from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.services.archivos import archivos
import time


class ModelsService:

    # Variables estaticas
    dir_reg = "./modelos_regresion/"
    dir_seg = "./modelos_onnx/"

    @staticmethod
    async def upload_reg_model(
        db: Session,
        reg_in: Any,
        user: models.User,
        model_file: File
    ):
        """ Crea un modelos de regresion en la BDD y el sistema de archivos
        """
        print("------------------ssd")
        # Se escribe el archivo por partes y se obtiene su ubicacion
        timestr = time.strftime("%Y%m%d_%H%M%S")
        ubicacion = f"{ModelsService.dir_reg}{timestr}.onnx"

        # Metodo asincrono de escritura de archivos
        await archivos.write_file(ubicacion, model_file)

        # Se agrega la ruta de creación
        regin = schemas.RegModelCreate(
            **dict(reg_in),
            file_path=ubicacion
        )

        model = crud.reg_model.create_with_owner(
            db=db,
            obj_in=regin,
            owner_id=user
        )

        return model

    @staticmethod
    async def upload_seg_model(
        db: Session,
        seg_in: schemas.SegModelBase,
        user: models.User,
        model_file: File
    ):
        """ Crea un modelos de regresion en la BDD y el sistema de archivos
        """
        # Se escribe el archivo por partes y se obtiene su ubicacion
        timestr = time.strftime("%Y%m%d_%H%M%S")
        ubicacion = f"{ModelsService.dir_seg}{timestr}.onnx"

        # Metodo asincrono de escritura de archivos
        await archivos.write_file(ubicacion, model_file)

        # Se agrega la ruta de creación
        regin = schemas.SegModelCreate(
            **dict(seg_in),
            file_path=ubicacion
        )

        model = crud.seg_model.create_with_owner(
            db=db,
            obj_in=regin,
            owner_id=user
        )

        return model
