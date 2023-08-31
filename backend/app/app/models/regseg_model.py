from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base

from app.models.model import Model

class RegressionModel(Model):
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    __tablename__="regressionmodel"
    accuracy: int = Column(Integer) # Precision de la segmentacion

    __mapper_args__ = {
        "polymorphic_identity": "regressionmodel"
    }

    def __init__(
            self,
            rmse,
            **kwargs,            
            ):
        super().__init__(**kwargs)
        self.rmse = rmse
        self.root_dir = "./modelos_onnx/"

class SegmentationModel(Model):
    __tablename__="segmentationmodel"
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    iou: int = Column(Integer) # Precision de la segmentacion
    
    __mapper_args__ = {
        "polymorphic_identity": "segmentationmodel"
    }

    def __init__(self):
        self.root_dir = "./modelos_regresion/"