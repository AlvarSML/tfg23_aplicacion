from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

from app.models.model import Model
from app.models.regseg_model import RegressionModel, SegmentationModel

from app.crud.crud_reg_model import reg_model
from app.crud.crud_seg_model import seg_model

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
    
    db.query(RegressionModel).delete()
    db.query(Model).delete()

    model_in1 = schemas.RegModelCreate(
        name="Resnet18_init",
        short_desc="Modelo de regresion",
        description="Modelo de regresion basado en resnet con 18 capas",
        file_path="./modelos_regresion/resnet34.onnx",
        rmse=12.0
    )

    model_in2 = schemas.RegModelCreate(
        name="Resnet18_init2",
        short_desc="Modelo de regresion2",
        description="Modelo de regresion basado en resnet con 18 capas",
        file_path="./modelos_regresion/resnet34.onnx",
        rmse=15.0
    )
    
    model1 = reg_model.create_with_owner(db=db, obj_in=model_in1, owner_id=user)
    model2 = reg_model.create_with_owner(db=db, obj_in=model_in2, owner_id=user)

    model_in1 = schemas.SegModelCreate(
        name="Yolo",
        short_desc="Modelo de regresion",
        description="Modelo de regresion basado en resnet con 18 capas",
        file_path="./modelos_regresion/resnet34.onnx",
        iou=.8
    )

    model_in2 = schemas.SegModelCreate(
        name="Detectron",
        short_desc="Modelo de regresion2",
        description="Modelo de regresion basado en resnet con 18 capas",
        file_path="./modelos_regresion/resnet34.onnx",
        iou=.9
    )    

    model1 = seg_model.create_with_owner(db=db, obj_in=model_in1, owner_id=user)
    model2 = seg_model.create_with_owner(db=db, obj_in=model_in2, owner_id=user)