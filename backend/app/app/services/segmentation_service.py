"""
Este modulo contiene el servicio de segmentacion de imagenes por medio de un modelo indeterminado
"""
from fastapi import UploadFile
from PIL import Image
import io
import pandas as pd
import numpy as np
import cv2

from app.services.YOLOSeg import YOLOSeg

# Instancia global?
modelo = None

def cargar_modelo(path:str, confidence=.3, iou=.5, func_medicion= lambda x: 10) -> YOLOSeg:
    """ Instancia un modelo de segmentacion ONNX
    """
    return YOLOSeg(
        path, 
        conf_thres=confidence, 
        iou_thres=iou,
        num_masks=32,
        func_medicion=func_medicion)

def cargar_imagen(file: UploadFile):
    """ Carga una imagen en formato PIL para introducir en el modelo
    """
    pil_img = Image.open(file.file).convert('RGB')
    cv_img = np.array(pil_img) 
    return cv_img[:, :, ::-1].copy()

def procesar_salida(file):
    """ Convierte una imagen de opencv a una enviable por la api
    """
    res, im_png = cv2.imencode(".jpeg", file)
    return im_png


