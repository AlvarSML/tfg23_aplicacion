import math
import time
import cv2
import numpy as np
import onnxruntime
from PIL import Image

import torchvision.transforms as transforms
from app.services.Padding import Padding

class ModeloReg:
    """ Representa un modelo de regresion bajo el formato onnx
    """
    def __init__(self, path:str) -> None:
        self.initialize_model(path)

    def __call__(self, image):
        return self.inference(self.prepare_input(image))

    def initialize_model(self, path) -> None:
        """ Instancia una sesion de onnx
        """
        self.session = onnxruntime.InferenceSession(path,
                                                    providers=['CUDAExecutionProvider',
                                                               'CPUExecutionProvider'])
        # Get model info
        self.get_input_details()
        self.get_output_details()

    def get_input_details(self):
        """ Obtiene las entradas del modelo
        """
        model_inputs = self.session.get_inputs()
        self.input_names = [model_inputs[i].name for i in range(len(model_inputs))]

        self.input_shape = model_inputs[0].shape
        self.input_height = self.input_shape[2]
        self.input_width = self.input_shape[3]

    def get_output_details(self):
        """ Obtiene las salidas del modelo
        """
        model_outputs = self.session.get_outputs()
        self.output_names = [model_outputs[i].name for i in range(len(model_outputs))]

    def inference(self, input_tensor):
        """ Ejecuta el modelo sobre una imagen
        """
        start = time.perf_counter()
        outputs = self.session.run(self.output_names, {self.input_names[0]: input_tensor})

        # print(f"Inference time: {(time.perf_counter() - start)*1000:.2f} ms")
        return outputs
    
    def prepare_input(self, image):
        """ Convierte la imagen en un tensor
        """
        self.img_height, self.img_width = image.shape[:2]

        # Debe ser una imagen PIL para torch
        image = Image.fromarray(image)        

        #input_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Aplicar el padding
        transformaciones = transforms.Compose([
            Padding(),
            transforms.Resize(size=256),
            transforms.ToTensor(),
            transforms.Normalize([0.5, ], [0.5, ])
        ])
        
        input_img = transformaciones(image)
 
        input_img = input_img.detach().cpu().numpy()

        # Transformaciones antiguas
        # Scale input pixel values to 0 to 1
        
        input_img = input_img / 255.0
        # input_img = input_img.transpose(2, 0, 1)
        input_img = input_img[np.newaxis, :, :, :].astype(np.float32)
        print(input_img)
        print(input_img.shape)
        
        return input_img