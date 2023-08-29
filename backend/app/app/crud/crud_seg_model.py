from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.regseg_model import SegmentationModel
from app.schemas.segmentation_model import SegModelCreate, SegModelUpdate

class CRUDRegModel(CRUDBase[SegmentationModel, RegModelCreate, RegModelUpdate]):

    def create_with_owner(
        self, db: Session, *, obj_in: RegModelCreate, owner_id: int
    ) -> SegmentationModel:
        """ Crea un modelo en la BDD
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_all(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[SegmentationModel]:
        """ Lista todos los modelos disponibles
        """
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

reg_model = CRUDRegModel(RegressionModel)