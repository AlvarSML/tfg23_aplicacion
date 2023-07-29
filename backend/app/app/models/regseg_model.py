from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped

from app.db.base_class import Base

from app.models.model import Model

# tabla para asociar los modelos compatibles de segmetnacion y regresion
association_seg_reg = Table(
    "association_seg_reg",
    Base.metadata,
    Column("modelo_seg", ForeignKey("regressionmodel.id"), primary_key=True),
    Column("modelo_reg", ForeignKey("segmentationmodel.id"), primary_key=True),
)

class RegressionModel(Model):
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    accuracy: int = Column(Integer) # Precision de la segmentacion
    segmentation_models: Mapped[List["segmentationmodel"]] = relationship(
        "SegmentationModel",
        secondary=association_seg_reg, 
        back_populates="regression_models")

    __mapper_args__ = {
        "polymorphic_identity": "regressionmodel",
    }

class SegmentationModel(Model):
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    accuracy: int = Column(Integer) # Precision de la segmentacion
    regression_models: Mapped[List["regressionmodel"]] = relationship(
        "RegressionModel",
        secondary=association_seg_reg, 
        back_populates="segmentation_models")
    
    __mapper_args__ = {
        "polymorphic_identity": "segmentationmodel",
    }