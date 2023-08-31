from typing import Optional
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath
from .model import ModelBase

class SegModelBase(ModelBase):
    iou_score: float

class SegModelCreate(SegModelBase):
    iou_score: float

class SegModelUpdate(SegModelBase):
    iou_score: float

class SegModelInDBBase(SegModelBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
# TODO
class SegModel(SegModelInDBBase):
    pass


# Additional properties stored in DB
# TODO
class SegModelInDB(SegModelInDBBase):
    hashed_password: str