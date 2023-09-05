from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.model import Model
from app.models.regseg_model import RegressionModel, SegmentationModel
from app.schemas.model import ModelCreate, ModelUpdate

class CRUDModel(CRUDBase[Model, ModelCreate, ModelUpdate]):

    def create_with_owner(
        self, 
        db: Session,
        *, 
        obj_in: ModelCreate, 
        owner_id: int
    ) -> Model:
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
    ) -> List[Model]:
        """ Lista todos los modelos disponibles
        """
        query = db.query(self.model)\
        .offset(skip)\
        .limit(limit)\
        .all()

        return (
            query
        )

    def get_by_id(
            self, 
            db: Session, 
            id: int
            
    ) -> Model:
        return db.query(Model).get(id)

    def get_seg_by_id(
            self, 
            db: Session, 
            *, 
            id: int
    ) -> SegmentationModel:
        return db.query(SegmentationModel).get(id)

    def get_reg_by_id(
            self, 
            db: Session, 
            *, 
            id: int
    ) -> RegressionModel:
        return db.query(RegressionModel).get(id)
model = CRUDModel(Model)