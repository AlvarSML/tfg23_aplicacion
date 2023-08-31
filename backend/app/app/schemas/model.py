from typing import Optional, Any
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath
from fastapi import Form, File, UploadFile



# Propiedades comunes
# TODO: Concretar filepath y dirpath
class ModelBase(BaseModel):
    name: str
    short_desc: str  # Descripcion corta para los menus
    model_description: Optional[str]  # Descripcion completa
    file_path: str


# Datos para la creacion de un modelo, nunca se modifican
# TODO: Subir archivo
class ModelCreate(ModelBase):
    file_path: str   # Establece el archivo especifico

# Properties to receive via API on update
class ModelUpdate(ModelBase):
    name: str
    short_desc: str  # Descripcion corta para los menus
    description: str  # Descripcion completa


class ModelInDBBase(ModelBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
# TODO
class Model(ModelInDBBase):
    pass


# Additional properties stored in DB
# TODO
class ModelInDB(ModelInDBBase):
    hashed_password: str
