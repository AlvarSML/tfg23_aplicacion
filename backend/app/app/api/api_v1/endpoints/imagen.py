from typing import Any, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse

import os
import io
import json
import cv2

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from PIL import Image

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

from app.services.segmentation_service import cargar_imagen, cargar_modelo
from app.services.regression_service import cargar_modelo_regresion

router = APIRouter()

@router.post("/subir/")
async def create_upload_file(image: UploadFile):
    destination_file_path = "/tmp/"+image.filename

    reg = cargar_modelo_regresion("./modelos_regresion/resnet34.onnx")
    modelo = cargar_modelo(
        path="./modelos_onnx/segmentacino_15.onnx",
        confidence=.30,
        iou=.50,
        func_medicion=reg)    

    img = cargar_imagen(image)
    res = modelo(img)
    anotada = modelo.draw_detections(img)
   
    res, im_png = cv2.imencode(".jpeg", anotada)
    


    #del modelo
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/jpeg")


@router.post("/dir/")
async def get_path():
    return(os.getcwd())