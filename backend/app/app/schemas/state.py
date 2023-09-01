from typing import Optional
from pydantic import BaseModel

from datetime import datetime
from app import models

# Propiedades comunes
# TODO: Concretar filepath y dirpath
class StateBase(BaseModel):
    seg_model: models.SegmentationModel
    reg_model: models.RegressionModel

    class Config:
        arbitrary_types_allowed = True

class StateCreate(StateBase):
    pass

class StatePaths(StateBase):
    seg_path: str
    reg_path: str

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
