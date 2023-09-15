from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base

from app.models.model import Model

if TYPE_CHECKING:
    from .state import ModelSelection  # noqa: F401

class RegressionModel(Model):
    id = Column(Integer, ForeignKey("model.id",  ondelete='cascade') ,primary_key=True)
    __tablename__="regressionmodel"
    rmse: float = Column(Float) 
    states: Mapped[List["ModelSelection"]] = relationship(
        "ModelSelection",
       back_populates="reg_model",
       cascade="all, delete"
    )
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
    id = Column(Integer, ForeignKey("model.id",  ondelete='cascade') ,primary_key=True)
    iou: float = Column(Float) # Precision de la segmentacion
    
    states: Mapped[List["ModelSelection"]] = relationship(
        "ModelSelection",
        back_populates="seg_model",
        cascade="all, delete"
    )
    __mapper_args__ = {
        "polymorphic_identity": "segmentationmodel"
    }

    def __init__(
            self,
            iou,
            **kwargs,            
            ):
        super().__init__(**kwargs)
        self.iou = iou
        self.root_dir = "./modelos_regresion/"