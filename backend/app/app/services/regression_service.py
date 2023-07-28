"""
Este modulo contiene el servicio de regresion de medidas un modelo indeterminado
"""

from fastapi import UploadFile
from PIL import Image
import io
import pandas as pd
import numpy as np
import cv2

from app.services.ModeloREG import ModeloReg

def cargar_modelo_regresion(path:str, confidence=.3, iou=.5) -> ModeloReg:
    """ Instancia un modelo de segmentacion ONNX
    """
    return ModeloReg(path)