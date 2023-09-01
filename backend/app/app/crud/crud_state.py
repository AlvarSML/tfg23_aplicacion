from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.state import ModelSelection
from app.schemas.state import State, StateCreate, StateBase, StatePaths

class CRUDState(CRUDBase[State, StateCreate, StateBase]):

    def create_with_owner(
        self, 
        db: Session,
        *, 
        obj_in: StateCreate, 
        owner_id: int
    ) -> ModelSelection:
        """ Crea un modelo en la BDD
        """
        print("ModelS",type(obj_in.seg_model))
        print("ModelR",type(obj_in.reg_model))
        db_obj = self.model(
            seg_model=obj_in.seg_model.id,
            reg_model=obj_in.reg_model.id, 
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
    ) -> State:
        """ Lista todos los modelos disponibles
        """
        stmt = select(self.model)\
            .join(self.model.seg_model)\
            .join(self.model.reg_model)\
            .order_by(self.model.created_date.desc())
        curr_state = db.execute(stmt).first()

        print("LAST",curr_state)

        base = State(
            seg_model= curr_state.ModelSelection.seg_model,
            reg_model= curr_state.ModelSelection.reg_model,
            changed_by= curr_state.ModelSelection.changed_by,
            created_date= curr_state.ModelSelection.created_date,
        )

        return base
    
    def get_current_paths(self, db:Session)-> StatePaths:
        stmt = select(self.model)\
            .join(self.model.seg_model)\
            .join(self.model.reg_model)\
            .order_by(self.model.created_date.desc())
        curr_state = db.execute(stmt).first()
        print("PATHS:",curr_state.ModelSelection.seg_model)
        """
        curr_state = db.query(self.model)\
            .order_by(self.model.created_date.desc())\
            .first()
        """
        paths = StatePaths(
            seg_model=curr_state.ModelSelection.seg_model,
            reg_model=curr_state.ModelSelection.reg_model,
            seg_path=curr_state.ModelSelection.reg_model.file_path,
            reg_path=curr_state.ModelSelection.seg_model.file_path,
        )
        print("PATHS:",paths)
        return paths

state = CRUDState(ModelSelection)