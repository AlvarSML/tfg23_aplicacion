import aiofiles
from fastapi import UploadFile, File
# Tiempo para los archivos
import time

class archivos:
    async def write_file(path:str, upload_file:UploadFile = File(...)) -> bool:
        """ Metodo asincrono para gestionar archivos
        """
        print(f"Escribiendo en ubicacion: {path}")
        try:
            # Guardado del modelo por parttes (Puede ser grande)
            async with aiofiles.open(path, 'wb') as out_file:
                while content := await upload_file.read(1024):  # async read chunk
                    await out_file.write(content)  # async write chunk
        except:
            return False
        else:
            return path