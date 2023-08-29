from typing import Optional
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath
from .model import ModelBase

class RegModelBase(ModelBase):
    rmse: int

class RegModelCreate(RegModelBase):
    rmse: int

class RegModelUpdate(RegModelBase):
    rmse: int

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