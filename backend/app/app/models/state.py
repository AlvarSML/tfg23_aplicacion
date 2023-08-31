from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import  Mapped, relationship, mapped_column
from sqlalchemy.sql import func

from app.db.base_class import Base

from .user import User
from .regseg_model import RegressionModel, SegmentationModel

class ModelSelection(Base):
    """ Representa un estado de modelo de regrsion y segmentacion
    """
    __tablename__="modelselection"
    id: int = Column(Integer, primary_key=True)
    created_date: DateTime = Column(DateTime(timezone=True), server_default=func.now())
    reg_model: Mapped["RegressionModel"] = mapped_column(ForeignKey("regressionmodel.id"))
    seg_model: Mapped["SegmentationModel"] = mapped_column(ForeignKey("segmentationmodel.id"))
    changed_by: Mapped["User"] = mapped_column(ForeignKey("user.id"))

    def __init__(
            self,
            reg_model,
            seg_model,
            owner_id
    ):
        self.reg_model = reg_model
        self.seg_model = seg_model
        self.changed_by = owner_id
