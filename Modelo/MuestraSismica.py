from datetime import datetime
from typing import List
from Modelo.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: datetime):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalles: List[DetalleMuestraSismica] = []
