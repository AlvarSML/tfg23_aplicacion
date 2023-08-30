from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import  Mapped, relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

from .user import User

class ModelSelection(Base):
    """ Representa un estado de modelo de regrsion y segmentacion
    """
    __tablename__="modelselection"
    id: int = Column(Integer, primary_key=True)
    created_date: Column(DateTime, default=func.now())
    reg_model =Column(Integer, ForeignKey("regressionmodel.id"))
    #seg_model: "SegmentationModel" = relationship("Model")
    changed_by: Mapped["User"] = relationship("User")
