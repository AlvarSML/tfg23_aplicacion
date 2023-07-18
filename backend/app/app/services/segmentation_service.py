"""
Este modulo contiene el servicio de segmentacion de imagenes por medio de un modelo indeterminado
"""
from fastapi import UploadFile
from PIL import Image
import io
import pandas as pd
import numpy as np

def procesar_imagen(file: UploadFile):
    """
    Obtiene la segmentacion de una imagen en base a un objeto UploadFile de FastAPI
    """
    with Image.open(file.file) as img_org:

def obtener_segmentos(
        modelo: Modelo
):