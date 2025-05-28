from datetime import datetime
from Modelo.Estado import Estado

class CambioEstado:
    def __init__(self, fechaHoraInicio: datetime, fechaHoraFin: datetime):
        self.fechaHoraInicio = fechaHoraInicio # datetime
        self.fechaHoraFin = fechaHoraFin # datetime
        self.estado = None # Puntero a objeto Estado

    def setEstado(self, estado):
        self.estado = estado

    def esEstadoActual(self):
        return self.fechaHoraFin is None

    def esAutoDetectado(self):
        return self.estado.esAutoDetectado()

    def setFechaHoraFin(self, fechaHoraFin):
        self.fechaHoraFin = fechaHoraFin
    
    