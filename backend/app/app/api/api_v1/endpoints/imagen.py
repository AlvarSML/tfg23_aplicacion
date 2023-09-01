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


from app.services.segmentation_service import cargar_imagen, cargar_modelo, procesar_salida
from app.services.regression_service import cargar_modelo_regresion

router = APIRouter()

@router.post("/subir/")
async def create_upload_file(
    image: UploadFile,
    db: Session = Depends(deps.get_db)):

    estado = crud.crud_state.state.get_last(db=db)
    print(estado)

    reg = cargar_modelo_regresion(estado.reg_model.file_path)
    modelo = cargar_modelo(
        path=estado.seg_model.file_path,
        confidence=.30,
        iou=.50,
        func_medicion=reg)    

    img = cargar_imagen(image)
    res = modelo(img)
    anotada = modelo.draw_detections(img)
    imagen_api = procesar_salida(anotada)

    #del modelo
    return StreamingResponse(io.BytesIO(imagen_api.tobytes()), media_type="image/jpeg")


@router.post("/dir/")
async def get_path():
    return(os.getcwd())