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
router = APIRouter()

@router.post("/subir/")
async def create_upload_file(file: UploadFile):
    destination_file_path = "/tmp/"+file.filename
    print(file)
    modelo = cargar_modelo("./modelos_onnx/segmentacino_15.onnx")
    img = cargar_imagen(file)
    res = modelo(img)
    combined_img = modelo.draw_masks(img)
    im_png = modelo.print_masks(img)[0]
    res, im_png = cv2.imencode(".jpg", im_png)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/jpg")


@router.post("/dir/")
async def get_path():
    return(os.getcwd())