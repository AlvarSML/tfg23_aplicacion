from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.model import Model

class RegressionModel(Model):
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    accuracy: int = Column(Integer) # Precision de la segmentacion
