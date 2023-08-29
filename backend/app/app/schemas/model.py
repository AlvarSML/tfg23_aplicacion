from typing import Optional, Any
from pydantic import BaseModel, EmailStr,  FilePath, DirectoryPath


# Propiedades comunes
# TODO: Concretar filepath y dirpath
class ModelBase(BaseModel):
    name: str
    short_desc: str  # Descripcion corta para los menus
    description: Optional[str]  # Descripcion completa
    file_path: FilePath


# Datos para la creacion de un modelo, nunca se modifican
# TODO: Subir archivo
class ModelCreate(ModelBase):
    root_dir: DirectoryPath # Establece el directorio base, por lo general no se modifica
    file_path: FilePath # Establece el archivo especifico
    model_file: Any # No se puede establecer el tipo de archivo

# Properties to receive via API on update
class ModelUpdate(ModelBase):
    name: str
    short_desc: str  # Descripcion corta para los menus
    description: Optional[str]  # Descripcion completa


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
