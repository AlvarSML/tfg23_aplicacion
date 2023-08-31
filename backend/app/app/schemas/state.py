from typing import Optional
from pydantic import BaseModel


# Propiedades comunes
# TODO: Concretar filepath y dirpath
class StateBase(BaseModel):
    seg_model: int
    reg_model: int

class StateCreate(StateBase):
    pass

class StateInDBBase(StateBase):
    seg_model: int
    reg_model: int
    changed_by: int

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
