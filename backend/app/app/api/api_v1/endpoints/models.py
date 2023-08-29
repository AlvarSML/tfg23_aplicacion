
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

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
def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    reg_model_in: schemas.RegModelCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile
):
    # TODO
    pass

@router.post("/nuevo_modelo_seg", response_model=schemas.SegModel)
def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    reg_model_in: schemas.SegModelCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    # TODO
    pass