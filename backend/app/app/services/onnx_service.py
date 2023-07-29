""" Servicio abstracto orientado a servir de interfaz para instanciar caulquier modelo onnx
    Se proporciona la inicializacion del modelo, lo demas debe ser provisto en subclases
"""

import math
import time
from typing import Any
import cv2
import numpy as np
import onnxruntime

class ONNX_service:
    def __init__(self, path:str) -> None:
        # Initialize model
        self.initialize_model(path)
    
    def __call__(self, image: np.array) -> Any:
        """ Ejecuta la inferencia sobre una imagen de entrada
        """
        return self.inference(image)

    def initialize_model(self, path:str):
        self.session = onnxruntime.InferenceSession(path,
                                                    providers=['CUDAExecutionProvider',
                                                               'CPUExecutionProvider'])
        self.get_input_details() # Obtiene los parametros de entrada
        self.get_output_details() # Obtiene las salidas

    def get_input_details(self):
        """ Obtiene el formato de la/s entrada/s del modelo
            Paso necesario para obtener las dimensiones para el reescalado
            Se almacena como atributos del servicio
        """
        model_inputs = self.session.get_inputs()
        self.input_names = [model_inputs[i].name for i in range(len(model_inputs))]

        self.input_shape = model_inputs[0].shape
        self.input_height = self.input_shape[2]
        self.input_width = self.input_shape[3]

    def get_output_details(self):
        """ Obtiene las salidas 
        """
        model_outputs = self.session.get_outputs()
        self.output_names = [model_outputs[i].name for i in range(len(model_outputs))]


    def inference(self, image: np.array):
        pass

    def prepare_input(self, image: np.array):
        """ Crea un tensor a partir de una imagen bidimensional
            antes la redimensiona segun
        """
        self.img_height, self.img_width = image.shape[:2]

        input_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize input image
        input_img = cv2.resize(input_img, (self.input_width, self.input_height))

        # Scale input pixel values to 0 to 1
        input_img = input_img / 255.0
        input_img = input_img.transpose(2, 0, 1)
        input_tensor = input_img[np.newaxis, :, :, :].astype(np.float32)
        return input_tensor