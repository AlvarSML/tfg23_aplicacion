from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.state import ModelSelection
from app.schemas.state import StateCreate, StateBase

class CRUDModel(CRUDBase[ModelSelection, StateCreate, StateBase]):

    def create_with_owner(
        self, 
        db: Session,
        *, 
        obj_in: StateCreate, 
        owner_id: int
    ) -> ModelSelection:
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
    ) -> List[ModelSelection]:
        """ Lista todos los modelos disponibles
        """
        query = db.query(self.model)\
        .offset(skip)\
        .limit(limit)\
        .all()

        print("*****Query",query)
        return (
            query
        )

state = CRUDModel(ModelSelection)