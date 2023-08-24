import numpy as np
import cv2
from PIL import Image

# TODO: Mover a la clase
class_names = ['diente', 'muela', 'raiz']

# Create a list of colors for each class where each color is a tuple of 3 integer values
rng = np.random.default_rng(3)
colors = rng.uniform(0, 255, size=(len(class_names), 3))


def nms(boxes, scores, iou_threshold):
    # Sort by score
    sorted_indices = np.argsort(scores)[::-1]

    keep_boxes = []
    while sorted_indices.size > 0:
        # Pick the last box
        box_id = sorted_indices[0]
        keep_boxes.append(box_id)

        # Compute IoU of the picked box with the rest
        ious = compute_iou(boxes[box_id, :], boxes[sorted_indices[1:], :])

        # Remove boxes with IoU over the threshold
        keep_indices = np.where(ious < iou_threshold)[0]

        # print(keep_indices.shape, sorted_indices.shape)
        sorted_indices = sorted_indices[keep_indices + 1]

    return keep_boxes


def compute_iou(box, boxes):
    # Compute xmin, ymin, xmax, ymax for both boxes
    xmin = np.maximum(box[0], boxes[:, 0])
    ymin = np.maximum(box[1], boxes[:, 1])
    xmax = np.minimum(box[2], boxes[:, 2])
    ymax = np.minimum(box[3], boxes[:, 3])

    # Compute intersection area
    intersection_area = np.maximum(0, xmax - xmin) * np.maximum(0, ymax - ymin)

    # Compute union area
    box_area = (box[2] - box[0]) * (box[3] - box[1])
    boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    union_area = box_area + boxes_area - intersection_area

    # Compute IoU
    iou = intersection_area / union_area

    return iou


def xywh2xyxy(x):
    # Convert bounding box (x, y, w, h) to bounding box (x1, y1, x2, y2)
    y = np.copy(x)
    y[..., 0] = x[..., 0] - x[..., 2] / 2
    y[..., 1] = x[..., 1] - x[..., 3] / 2
    y[..., 2] = x[..., 0] + x[..., 2] / 2
    y[..., 3] = x[..., 1] + x[..., 3] / 2
    return y


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def recortar_bbox(image, boxes, scores, class_ids):
    dientes = []
    for box, score, class_id in zip(boxes, scores, class_ids):
        if class_id == 0: # TODO: La id esta hardcodeada habria que revisarlo
            # Coordenadas de las esquinas de las cajas
            x1, y1, x2, y2 = box.astype(int)
            recortada = image[y1:y2,x1:x2]
            dientes.append(recortada)
    return dientes
    
def mascaras(image, boxes, scores, class_ids, masks ,mask_alpha=0.3):
    dientes = []
    for box, score, class_id, mask in zip(boxes, scores, class_ids, masks):
        if class_id == 0: # TODO: La id esta hardcodeada habria que revisarlo
            # Coordenadas de las esquinas de las cajas
            x1, y1, x2, y2 = box.astype(int)
            recortada = mask[y1:y2,x1:x2]
            recortada = Image.fromarray((recortada * 255).astype('uint8'))
            dientes.append(np.array(recortada))
    return dientes
