from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.state import ModelSelection
from app.schemas.state import StateCreate, StateBase, StatePaths

class CRUDState(CRUDBase[ModelSelection, StateCreate, StateBase]):

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
        db_obj = self.model(
            seg_model=obj_in.seg_model,
            reg_model=obj_in.reg_model, 
            owner_id=owner_id)
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

    def get_last(
        self, db: Session
    ) -> ModelSelection:
        """ Lista todos los modelos disponibles
        """
        query = db.query(self.model)\
            .order_by(self.model.created_date.desc())\
            .first()

        return query
    
    def get_current_paths(self, db:Session)-> StatePaths:
        stmt = select(self.model)\
            .join(self.model.seg_model)\
            .join(self.model.reg_model)\
            .order_by(self.model.created_date.desc())
        curr_state = db.execute(stmt).first()
        print("PATHS:",type(curr_state.ModelSelection.seg_model))
        """
        curr_state = db.query(self.model)\
            .order_by(self.model.created_date.desc())\
            .first()
        """
        paths = StatePaths(
            seg_model=curr_state.seg_model.id,
            reg_model=curr_state.reg_model.id,
            seg_path=curr_state.reg_model.file_path,
            reg_path=curr_state.seg_model.file_path,
        )
        print("PATHS:",paths)
        return paths

state = CRUDState(ModelSelection)