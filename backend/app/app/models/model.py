"""
Clase que modela un archivo onnx de un modelo de YOLO o pytorch
"""

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Model(Base):
    """ Representa cualquier modelo almacenado
    """
    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # Nombre del modelo (Ej.: YOLOm, resnet30)
    short_desc: str = Column(String, index=False) # Descripcion corta para los menus
    description: str = Column(String, index=False) # Descripcion completa
    root_dir: str = Column(String, index=False) # Establece el directorio base, por lo general no se modifica
    file_path = Column(String, index=True)
