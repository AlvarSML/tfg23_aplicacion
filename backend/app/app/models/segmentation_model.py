from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.model import Model
from app.models.regression_model import RegressionModel, association_seg_reg

class SegmentationModel(Model):
    id = Column(Integer, ForeignKey("model.id") ,primary_key=True)
    accuracy: int = Column(Integer) # Precision de la segmentacion
    regression_models: Mapped[List[RegressionModel]] = relationship(
        secondary=association_seg_reg, 
        back_populates="segmentation_models")