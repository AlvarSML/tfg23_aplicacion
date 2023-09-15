from typing import Any, List

from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.services import StatesService, archivos

router = APIRouter()
@router.get("/", response_model=schemas.StateInDBBase)
def get_last(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """ Devuleve el ultimo estado creado
    """
    models = crud.state.get_last(db)
    if models:
        return models
    else:
        raise HTTPException(status_code=404, detail="State not found")


@router.get("/all", response_model=List[schemas.StateInDBBase])
def get_states(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """ Devuleve todos los estados
        Requiere autorizacion
    """
    if crud.user.is_superuser(current_user):
        models = crud.state.get_all(db,owner_id=current_user,skip=skip,limit=limit)
    else:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return models

@router.post("/nuevo_estado", response_model=schemas.StateInDBBase)
async def post_state(
    *,
    db: Session = Depends(deps.get_db),
    state_in: schemas.StateCreate = Depends(),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """ Genera un nuevo estado
        Obsoleto: los modelos se cambian de 1 en 1
    """
    if crud.user.is_superuser(current_user):
        return crud.state.create_with_owner(db=db, obj_in=state_in, owner_id=current_user.id)
    else:
        raise HTTPException(status_code=403, detail="Not enough permissions")

@router.get("/paths", response_model=schemas.StatePaths)
def get_last(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """ Obtiene las rutas de los modelos actuales
        Obsoleto: se usa la ruta / para obtener el ultimo con todos los datos
    """
    if crud.user.is_superuser(current_user):
        models = crud.state.get_current_paths(db)
    else:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return models


@router.post("/change_reg",
            response_model=schemas.StateInDBBase, 
             responses={
                404: {
                    "model": schemas.Msg, 
                    "description": "No se encuentra el modelo que se quiere sustituir"
                },
                403: {
                    "model": schemas.Msg, 
                    "description": "El usuario no tiene permisos suficientes para modificar el estado"
                }
                })
async def change_reg(
    *,
    db: Session = Depends(deps.get_db),
    state_in: int = Body(embed=True),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """ Modifica el modelo de regresion del estado
    """
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para modificar el estado"})
    
    resp = StatesService.change_reg(db,state_in,current_user)
    if resp:
        return resp
    return JSONResponse(status_code=404, content={"message": "Modelo de regresion no encontrado"})


@router.post("/change_seg",
              response_model=schemas.StateInDBBase,
                responses={
                    404: {
                        "model": schemas.Msg, 
                        "description": "No se encuentra el modelo que se quiere sustituir"
                    },
                    403: {
                        "model": schemas.Msg, 
                        "description": "El usuario no tiene permisos suficientes para modificar el estado"
                    }                    
                  })
async def change_seg(
    *,
    db: Session = Depends(deps.get_db),
    state_in: int = Body(embed=True),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """ Modifica el modelo de segmentacion del estado
    """
    if not crud.user.is_superuser(current_user):
        return JSONResponse(status_code=403, content={"message": "El usuario no tiene permisos para modificar el estado"})

    resp = StatesService.change_seg(db,state_in,current_user)
    if resp:
        return resp
    return JSONResponse(status_code=404, content={"message": "Modelo de segmentacion no encontrado"})