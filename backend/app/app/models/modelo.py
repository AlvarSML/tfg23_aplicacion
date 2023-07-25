"""
Clase que modela un archivo onnx de un modelo de YOLO o pytorch
"""

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Modelo(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=False)
    file_path = Column(String, index=True)
