from typing import Optional
from pydantic import BaseModel

from datetime import datetime
from app import models, schemas

# Propiedades comunes
# TODO: Concretar filepath y dirpath
class StateBase(BaseModel):
    seg_model: schemas.SegModel
    reg_model: schemas.RegModel

class StateCreate(StateBase):
    pass

class StatePaths(StateBase):
    seg_path: str
    reg_path: str

# Como se devuelven los datos de la bdd
class StateInDBBase(StateBase):
    seg_model: schemas.SegModel
    reg_model: schemas.RegModel
    changed_by: int
    created_date: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
# TODO
class State(StateInDBBase):
    pass


# Additional properties stored in DB
# TODO
class StateInDB(StateInDBBase):
    pass
