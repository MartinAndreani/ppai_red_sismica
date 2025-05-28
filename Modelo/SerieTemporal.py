from datetime import datetime
from typing import List
from Modelo.MuestraSismica import MuestraSismica
from Modelo.Sismografo import Sismografo

class SerieTemporal:
    def __init__(self, condicionAlarma: bool, fechaHoraInicioMuestras: datetime, frecuenciaMuestreo: str): 
        self.condicionAlarma = condicionAlarma # bool
        self.fechaHoraInicioMuestras = fechaHoraInicioMuestras # datetime
        self.muestras: List[MuestraSismica] = [] # lista de punteros a objetos MuestraSismica
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.sismografo = None # puntero a objeto Sismografo
        
    def setSismografo(self, sismografo):
        self.sismografo = sismografo
        
    def getNombreEstacionSismologica(self):
        return self.sismografo.getNombreEstacionSismologica()
        
    def getDatos(self):
        return {
            'fechaHoraInicio': self.fechaHoraInicioMuestras,
            'sismografo': self.sismografo.identificadorSismografo,
            'muestras': [muestra.getDatos() for muestra in self.muestras]
        }