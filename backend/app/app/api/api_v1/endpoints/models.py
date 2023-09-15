from typing import Any, List

from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.services import archivos, ModelsService
import time

# TODO: mover a configuracion
dir_seg = "./modelos_onnx/"
dir_reg = "./modelos_regresion/"

router = APIRouter()


@router.get("/",
            response_model=List[schemas.Model],
            responses={
                403: {
                    "model": schemas.Msg,
                    "description": "El usuario no tiene permisos suficientes para leer los modelos"
                }
            })
def get_models(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if crud.user.is_superuser(current_user):
        models = crud.model.get_all(
            db, owner_id=current_user, skip=skip, limit=limit)
    else:
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para modificar el estado"})
    return models


@router.post("/nuevo_modelo_reg",
             response_model=schemas.RegModel,
             responses={
                 403: {
                     "model": schemas.Msg,
                     "description": "El usuario no tiene permisos suficientes para leer los modelos"
                 },
                 500: {
                     "model": schemas.Msg,
                     "description": "Error desconocido del servidor"
                 },
                 507: {
                     "model": schemas.Msg,
                     "description": "Error de escritura del archivo"
                 }
             })
async def post_reg_model(
    *,
    db: Session = Depends(deps.get_db),
    reg_model_in: schemas.RegModelBase = Depends(),
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile
):
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para crear modelos"})

    resp = await ModelsService.upload_reg_model(
        db=db,
        reg_in=reg_model_in,
        user=current_user,
        model_file=model_file
    )

    if resp:
        return resp
    else:
        return JSONResponse(status_code=500, content={"message": "Error desconocido"})


@router.post(
    "/nuevo_modelo_seg",
    response_model=schemas.SegModel,
    responses={
        403: {
            "model": schemas.Msg,
            "description": "El usuario no tiene permisos suficientes para leer los modelos"
        },
        500: {
            "model": schemas.Msg,
            "description": "Error desconocido del servidor"
        },
        507: {
            "model": schemas.Msg,
            "description": "Error de escritura del archivo"
        }
    })
async def post_seg_model(
    *,
    db: Session = Depends(deps.get_db),
    seg_model_in: schemas.SegModelBase = Depends(),
    current_user: models.User = Depends(deps.get_current_active_user),
    model_file: UploadFile
):
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para crear modelos"})

    resp = await ModelsService.upload_seg_model(
        db=db,
        seg_in=seg_model_in,
        user=current_user,
        model_file=model_file
    )

    if resp:
        return resp
    else:
        return JSONResponse(status_code=500, content={"message": "Error desconocido"})


@router.get(
    "/get_regression",
    response_model=List[schemas.RegModel],
    responses={
        403: {
            "model": schemas.Msg,
            "description": "El usuario no tiene permisos suficientes para leer los modelos"
        },
        404: {
            "model": schemas.Msg,
            "description": "No existe ningun modelo de regresion"
        }
    })
async def get_regression(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
):
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para consultar los modelos"})

    model = crud.reg_model.get_all(
        db, owner_id=current_user, skip=skip, limit=limit)
    return model or JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para consultar los modelos"})


@router.get(
    "/get_model_id",
    response_model=schemas.Model,
    responses={
        403: {
            "model": schemas.Msg,
            "description": "El usuario no tiene permisos suficientes para leer los modelos"
        },
        404: {
            "model": schemas.Msg,
            "description": "No existe ningun modelo con ese identificador"
        }
    })
async def get_model_id(
    db: Session = Depends(deps.get_db),
    id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user)
):
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para consultar los modelos"})

    model = crud.model.get_by_id(db, id)
    return model or JSONResponse(status_code=404, content={"message": f"No existe ningun modelo con ese identificado: {id}"})


@router.get(
    "/get_segmentation",
    response_model=List[schemas.SegModel],
    responses={
        403: {
            "model": schemas.Msg,
            "description": "El usuario no tiene permisos suficientes para leer los modelos"
        },
        404: {
            "model": schemas.Msg,
            "description": "No existe ningun modelo de segmentacion"
        }
    })
async def get_segmetation(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para consultar los modelos"})

    models = crud.seg_model.get_all(
        db, owner_id=current_user, skip=skip, limit=limit)
    return models  or JSONResponse(status_code=404, content={"message": f"No existen modelos de segementación"})

@router.delete(
    "delete/{model_id}",
    response_model=schemas.Model,
    responses={
        404: {
            "model": schemas.Msg,
            "description": "No existe ningun modelo con ese identificador"
        },
        507: {
            "model": schemas.Msg,
            "description": "Error de eliminacion"
        }
    }
)
async def del_model(
    db: Session = Depends(deps.get_db),
    *,
    model_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    deleted:schemas.Model = await ModelsService.delete_model(
        db=db,
        id=model_id,
        user=current_user
    )
    print("->Deleted",deleted)
    return deleted