from typing import Optional
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath
from .model import ModelBase

class SegModelBase(ModelBase):
    iou: float

class SegModelCreate(SegModelBase):
    file_path: str  
    iou: float

class SegModelUpdate(SegModelBase):
    iou: float

class SegModelInDBBase(SegModelBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
# TODO
class SegModel(SegModelInDBBase):
    file_path: str  
    pass


# Additional properties stored in DB
# TODO
class SegModelInDB(SegModelInDBBase):
    hashed_password: str