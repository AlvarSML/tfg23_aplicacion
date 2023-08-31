
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.services.archivos import archivos


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
    res = archivos.write_file(dir_reg, model_file)
    if res:
        
        model = crud.reg_model.create_with_owner(
            db=db,
            obj_in=reg_model_in,
            owner_id=current_user
        )
        return model
    else:
        raise HTTPException(
            status_code=502,
            detail="Error de escritura",
            headers={"X-Error": "There goes my error"},
        )


@router.post("/nuevo_modelo_seg", response_model=schemas.SegModel)
async def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    reg_model_in: schemas.SegModelCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile = File(...)
):
    archivos.write_file(dir_seg, model_file)
    return {"Result": "OK"}
