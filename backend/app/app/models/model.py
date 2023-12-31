"""
Clase que modela un archivo onnx de un modelo de YOLO o pytorch
"""

from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func

from app.db.base_class import Base


class Model(Base):
    """ Representa cualquier modelo almacenado
    """
    __tablename__="model"

    id: int = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String, index=True) # Nombre del modelo (Ej.: YOLOm, resnet30)
    short_desc: str = Column(String, index=False) # Descripcion corta para los menus
    model_description: str = Column(String, index=False) # Descripcion completa
    root_dir: str = Column(String, index=False) # Establece el directorio base, por lo general no se modifica
    file_path: str = Column(String, index=True) # Nombre del modelo desde el dir raiz

    def __init__(
            self,
            name,
            short_desc,
            model_description,
            file_path,
            ):
        self.name = name
        self.short_desc = short_desc
        self.model_description = model_description
        self.file_path = file_path
    
    def __repr__(self):
        return f"<Modelo: {self.name}>"
