from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.services.archivos import archivos
import time 


router = APIRouter()
@router.get("/", response_model=List[schemas.StateInDBBase])
def get_states(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if crud.user.is_superuser(current_user):
        models = crud.state.get_all(db,owner_id=current_user,skip=skip,limit=limit)
    else:
        models = []
    return models

@router.post("/nuevo_estado", response_model=schemas.StateInDBBase)
async def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    state_in: schemas.StateCreate = Depends(),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    statec = crud.state.create_with_owner(db=db, obj_in=state_in, owner_id=current_user.id)
    return statec


@router.post("/nuevo_modelo_seg", response_model=schemas.Model)
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