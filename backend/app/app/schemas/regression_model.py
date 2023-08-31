from typing import Optional
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath
from .model import ModelBase

class RegModelBase(ModelBase):
    rmse: float

class RegModelCreate(RegModelBase):
    rmse: float

class RegModelUpdate(RegModelBase):
    rmse: float

class RegModelInDBBase(RegModelBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
# TODO
class RegModel(RegModelInDBBase):
    pass


# Additional properties stored in DB
# TODO
class RegModelInDB(RegModelInDBBase):
    hashed_password: str