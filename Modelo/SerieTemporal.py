from datetime import datetime
from typing import List
from Modelo.MuestraSismica import MuestraSismica

class SerieTemporal:
    def __init__(self, fechaHoraInicioMuestras: datetime): 
        self.fechaHoraInicioMuestras = fechaHoraInicioMuestras # datetime
        self.muestras: List[MuestraSismica] = [] # Lista de punteros a objetos MuestraSismica
        
