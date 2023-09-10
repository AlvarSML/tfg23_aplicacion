from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas

class StatesService:
  """ Gestiona las operaciones de los estados que requieran pasos intermedios
  """
  def change_reg(db: Session, reg_model: int, current_user:models.User) -> schemas.StateInDBBase:
    """ Modifica el modelo de regresion del último estado
    """
    last_state = crud.state.get_last(db)
    new_reg_model = crud.model.get_by_id(db, reg_model)

    if new_reg_model:
      last_state.reg_model = new_reg_model
      new_state = crud.state.create_with_owner(db=db, obj_in=last_state, owner_id=current_user.id)
      return new_state
    else:
      raise HTTPException(status_code=404, detail="Nuevo modelo no encontrado")