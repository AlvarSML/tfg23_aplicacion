import aiofiles
from fastapi import UploadFile, File, HTTPException
# Tiempo para los archivos
import time
import os

class archivos:
    async def write_file(path:str, upload_file:UploadFile = File(...)) -> bool:
        """ Metodo asincrono para gestionar archivos
        """
        # print(f"Escribiendo en ubicacion: {path}")
        try:
            # Guardado del modelo por parttes (Puede ser grande)
            async with aiofiles.open(path, 'wb') as out_file:
                while content := await upload_file.read(1024 * 1000):  # lee por bloques de 1MB para evitar colapsar con archivos grandes
                    await out_file.write(content)  # async write chunk
        except:
            raise HTTPException(status_code=507, detail="Error de escritura del modelo")
        else:
            return path
        
    async def del_file(path:str):
        """ Metodo asincrono para eliminar
        """
        try:
            if os.path.exists(path):
                os.remove(path)
            else:
                raise HTTPException(status_code=507, detail="El modelo a eliminar no existe")
        except:
            raise HTTPException(status_code=507, detail="Error en la eliminacion del modelo")