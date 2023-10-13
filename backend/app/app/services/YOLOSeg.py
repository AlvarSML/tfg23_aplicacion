import math
import time
import cv2
import numpy as np
import onnxruntime

from app.services.utils import *

""" TODO: Implementar ONNX_service
"""


class YOLOSeg:
    """ Clase que gestiona las operaciones sobre una imagen
    """
    def __init__(
            self, 
            path,
            conf_thres = 0.7, 
            iou_thres = 0.5, 
            num_masks = 32, 
            func_medicion = lambda x: 10,
            class_names = ['diente', 'muela', 'raiz']
            ):
        self.conf_threshold = conf_thres
        self.iou_threshold = iou_thres
        self.num_masks = num_masks

        # Funcion de medicion por inyecccion de dependencias
        # Debe ser un modelo oxxn
        self.func_medicion = func_medicion

        # Por defecto onnx numera las labels
        self.class_names = class_names

        # Colores de dibujo
        rng = np.random.default_rng(3)
        self.colors = rng.uniform(0, 255, size=(len(class_names), 3))

        # Initialize model
        self.initialize_model(path)


    def __call__(self, image):
        self.segment_objects(image)
        self.measure_elements(
            self.mask_maps,
            self.class_ids,
            [0])

    def initialize_model(self, path):
        self.session = onnxruntime.InferenceSession(path,
                                                    providers=['CUDAExecutionProvider',
                                                               'CPUExecutionProvider'])
        # Get model info
        self.get_input_details()
        self.get_output_details()

    def segment_objects(self, image):
        """ Operacion de inferencia de segmentacion sobre la imagen
        """
        input_tensor = self.prepare_input(image)

        # Perform inference on the image
        outputs = self.inference(input_tensor)

        self.boxes, self.scores, self.class_ids, mask_pred = self.process_box_output(outputs[0])
        self.mask_maps = self.process_mask_output(mask_pred, outputs[1])

        return self.boxes, self.scores, self.class_ids, self.mask_maps

    def measure_elements(self, parts_crops, class_ids, class_obj):
        """ Aplica las mediciones si la clase que se encuentra esta en class_obj
            Introducir todas las mascaras par mantener el orden de las mediciones
        Parameters
        ----------
        parts_crops: img
            recortes de la imagen original que van a ser procesados por la funcion de medicion

        class_ids: arr[int]
            ids de las clases de la segmetnacion previa
        
        class_obj: arr[int]
            ids objetivo de las clases que van a ser medidasd
        
        Returns
        -------
        list
            lista de mediciones de todos los recortes, los no objetivo se encontraran a -1

        """
        measures = []
        for part, clas in zip(parts_crops, class_ids):
            if clas in class_obj:
                measures.append(self.func_medicion(part))
            else:
                measures.append(-1)
        self.measures = measures
        return self.measures


    def prepare_input(self, image):
        """ Transforma la imagen de entrada en un tensor
            Se debe modificar en caso de usar otras dimensiones
            Usa la libreria CV2
        """
        self.img_height, self.img_width = image.shape[:2]

        input_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize input image
        input_img = cv2.resize(input_img, (self.input_width, self.input_height))

        # Scale input pixel values to 0 to 1
        input_img = input_img / 255.0
        input_img = input_img.transpose(2, 0, 1)
        input_tensor = input_img[np.newaxis, :, :, :].astype(np.float32)

        return input_tensor

    def inference(self, input_tensor):
        start = time.perf_counter()
        outputs = self.session.run(self.output_names, {self.input_names[0]: input_tensor})

        # print(f"Inference time: {(time.perf_counter() - start)*1000:.2f} ms")
        return outputs

    def process_box_output(self, box_output):

        predictions = np.squeeze(box_output).T
        num_classes = box_output.shape[1] - self.num_masks - 4

        # Filter out object confidence scores below threshold
        scores = np.max(predictions[:, 4:4+num_classes], axis=1)
        predictions = predictions[scores > self.conf_threshold, :]
        scores = scores[scores > self.conf_threshold]

        if len(scores) == 0:
            return [], [], [], np.array([])

        box_predictions = predictions[..., :num_classes+4]
        mask_predictions = predictions[..., num_classes+4:]

        # Get the class with the highest confidence
        class_ids = np.argmax(box_predictions[:, 4:], axis=1)

        # Get bounding boxes for each object
        boxes = self.extract_boxes(box_predictions)

        # Apply non-maxima suppression to suppress weak, overlapping bounding boxes
        indices = nms(boxes, scores, self.iou_threshold)

        return boxes[indices], scores[indices], class_ids[indices], mask_predictions[indices]

    def process_mask_output(self, mask_predictions, mask_output):
        """ Escala las mascaras para mostrarlas sobre el tamaño original y no el escalado
        """
        if mask_predictions.shape[0] == 0:
            return []

        mask_output = np.squeeze(mask_output)

        # Calculate the mask maps for each box
        num_mask, mask_height, mask_width = mask_output.shape  # CHW
        masks = sigmoid(mask_predictions @ mask_output.reshape((num_mask, -1)))
        masks = masks.reshape((-1, mask_height, mask_width))

        # Downscale the boxes to match the mask size
        scale_boxes = self.rescale_boxes(self.boxes,
                                   (self.img_height, self.img_width),
                                   (mask_height, mask_width))

        # For every box/mask pair, get the mask map
        mask_maps = np.zeros((len(scale_boxes), self.img_height, self.img_width))
        blur_size = (int(self.img_width / mask_width), int(self.img_height / mask_height))
        for i in range(len(scale_boxes)):

            scale_x1 = int(math.floor(scale_boxes[i][0]))
            scale_y1 = int(math.floor(scale_boxes[i][1]))
            scale_x2 = int(math.ceil(scale_boxes[i][2]))
            scale_y2 = int(math.ceil(scale_boxes[i][3]))

            x1 = int(math.floor(self.boxes[i][0]))
            y1 = int(math.floor(self.boxes[i][1]))
            x2 = int(math.ceil(self.boxes[i][2]))
            y2 = int(math.ceil(self.boxes[i][3]))

            scale_crop_mask = masks[i][scale_y1:scale_y2, scale_x1:scale_x2]
            crop_mask = cv2.resize(scale_crop_mask,
                              (x2 - x1, y2 - y1),
                              interpolation=cv2.INTER_CUBIC)

            crop_mask = cv2.blur(crop_mask, blur_size)

            crop_mask = (crop_mask > 0.5).astype(np.uint8)
            mask_maps[i, y1:y2, x1:x2] = crop_mask

        return mask_maps

    def extract_boxes(self, box_predictions):
        # Extract boxes from predictions
        boxes = box_predictions[:, :4]

        # Scale boxes to original image dimensions
        boxes = self.rescale_boxes(boxes,
                                   (self.input_height, self.input_width),
                                   (self.img_height, self.img_width))

        # Convert boxes to xyxy format
        boxes = xywh2xyxy(boxes)

        # Check the boxes are within the image
        boxes[:, 0] = np.clip(boxes[:, 0], 0, self.img_width)
        boxes[:, 1] = np.clip(boxes[:, 1], 0, self.img_height)
        boxes[:, 2] = np.clip(boxes[:, 2], 0, self.img_width)
        boxes[:, 3] = np.clip(boxes[:, 3], 0, self.img_height)

        return boxes

    def draw_detections(self, image, draw_scores=True, mask_alpha=0.4):
        """ Dibujado sobre las imagenes, las mascaras deben ser escaladas previamente
            las mascaras se dibujan antes
            TODO: eliminar dibujado previo de mascaras
        """
        img_height, img_width = image.shape[:2]
        size = min([img_height, img_width]) * 0.0006
        size = 1.2

        text_thickness = int(min([img_height, img_width]) * 0.001)

        # Las mascaras son dibujadas con color
        mask_img = self.draw_masks(
            image,
            mask_alpha
            )

        # Dibujado de las BB
        alturas = [] # Comprueba las alturas de los textos   
        for box, score, class_id, measure in zip(self.boxes, self.scores, self.class_ids, self.measures):
            color = self.colors[class_id]

            x1, y1, x2, y2 = box.astype(int)

            if y2 < (50):
                y2 = y2 + 50

            if y1 < (50):
                y1 = y1 + 50

            # BB
            print("Rectangulo: ",y1,y2,"Real: ",img_height)
            cv2.rectangle(mask_img, (x1, y1), (x2, y2), color, 2)

            # Descripcion de cada deteccion
            label = self.class_names[class_id]
            caption = f'{label} {int(score * 100)}%'


            if measure != -1:
                caption += f' | {float(measure[0]):2.2f}mm'

            (tw, th), _ = cv2.getTextSize(text=caption, fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                        fontScale=size, thickness=text_thickness)
            th = int(th * 1.2)


            if len(alturas) > 0 and measure != -1:
                while  any(abs(x - y1) < 30 for x in alturas):
                    y1 += 30
            alturas.append(y1)

            cv2.rectangle(mask_img, (x1, y1),
                        (x1 + tw, y1 - th), color, -1)          

            
            cv2.putText(mask_img, caption, (x1, y1),
                        cv2.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv2.LINE_AA)

        return mask_img

    def draw_masks(self, image, draw_scores=True, mask_alpha=0.5):
        mask_img = image.copy()

        # Draw bounding boxes and labels of detectionsl
        for i, (box, class_id) in enumerate(zip(self.boxes, self.class_ids)):
            color = self.colors[class_id]

            x1, y1, x2, y2 = box.astype(int)

            # Draw fill mask image
            if self.mask_maps is None:
                cv2.rectangle(mask_img, (x1, y1), (x2, y2), color, -1)
            else:
                crop_mask =self.mask_maps[i][y1:y2, x1:x2, np.newaxis]
                crop_mask_img = mask_img[y1:y2, x1:x2]
                crop_mask_img = crop_mask_img * (1 - crop_mask) + crop_mask * color
                mask_img[y1:y2, x1:x2] = crop_mask_img

        return cv2.addWeighted(mask_img, mask_alpha, image, 1 - mask_alpha, 0)

    def print_masks(self, image, draw_scores=True, mask_alpha=0.5):
        return mascaras(
            image=image, 
            boxes=self.boxes, 
            scores=self.scores,
            class_ids=self.class_ids, 
            mask_alpha=mask_alpha, 
            masks=self.mask_maps)


    def crop_teeth(self,image):
        return recortar_bbox(
            image,
            self.boxes,
            self.scores,
            self.class_ids)

    def get_input_details(self):
        model_inputs = self.session.get_inputs()
        self.input_names = [model_inputs[i].name for i in range(len(model_inputs))]

        self.input_shape = model_inputs[0].shape
        self.input_height = self.input_shape[2]
        self.input_width = self.input_shape[3]

    def get_output_details(self):
        model_outputs = self.session.get_outputs()
        self.output_names = [model_outputs[i].name for i in range(len(model_outputs))]

    @staticmethod
    def rescale_boxes(boxes, input_shape, image_shape):
        # Rescale boxes to original image dimensions
        input_shape = np.array([input_shape[1], input_shape[0], input_shape[1], input_shape[0]])
        boxes = np.divide(boxes, input_shape, dtype=np.float32)
        boxes *= np.array([image_shape[1], image_shape[0], image_shape[1], image_shape[0]])

        return boxes
