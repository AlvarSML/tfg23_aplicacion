from typing import Optional
from pydantic import BaseModel

from datetime import datetime


# Propiedades comunes
# TODO: Concretar filepath y dirpath
class StateBase(BaseModel):
    seg_model: int
    reg_model: int

class StateCreate(StateBase):
    pass

# Como se devuelven los datos de la bdd
class StateInDBBase(StateBase):
    seg_model: int
    reg_model: int
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
