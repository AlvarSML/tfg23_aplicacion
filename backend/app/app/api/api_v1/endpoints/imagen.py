from typing import Any, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile


from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from PIL import Image

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

router = APIRouter()

@router.post("/subir/")
async def create_upload_file(file: UploadFile) -> Image:
    destination_file_path = "/tmp/"+file.filename
    print(file)
    img = Image.open(file.file)
    print(img)
    return img
