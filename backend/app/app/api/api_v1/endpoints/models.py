from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.services.archivos import archivos
import time 

# TODO: mover a configuracion
dir_seg = "./modelos_onnx/"
dir_reg = "./modelos_regresion/"

router = APIRouter()
@router.get("/", response_model=List[schemas.Model])
def get_models(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if crud.user.is_superuser(current_user):
        models = crud.model.get_all(db,owner_id=current_user,skip=skip,limit=limit)
    else:
        models = []
    return models

@router.post("/nuevo_modelo_reg", response_model=schemas.RegModel)
async def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    reg_model_in: schemas.RegModelCreate = Depends(),
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile  
):
    # Se escribe el archivo por partes y se obtiene su ubicacion
    timestr = time.strftime("%Y%m%d_%H%M%S")
    ubicacion = f"{dir_reg}{timestr}.onnx"

    # Metodo asincrono de escritura de archivos
    await archivos.write_file(ubicacion, model_file)
    reg_model_in.file_path = ubicacion

    model = crud.reg_model.create_with_owner(
        db=db,
        obj_in=reg_model_in,
        owner_id=current_user
    )
    return model


@router.post("/nuevo_modelo_seg", response_model=schemas.SegModel)
async def post_seg_model(
    *,
    db: Session = Depends(deps.get_db),
    seg_model_in: schemas.SegModelCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile = File(...)
):
     # Se escribe el archivo por partes y se obtiene su ubicacion
    timestr = time.strftime("%Y%m%d_%H%M%S")
    ubicacion = f"{dir_seg}{timestr}.onnx"

    # Metodo asincrono de escritura de archivos
    await archivos.write_file(ubicacion, model_file)
    seg_model_in.file_path = ubicacion

    model = crud.reg_model.create_with_owner(
        db=db,
        obj_in=seg_model_in,
        owner_id=current_user
    )
    return model