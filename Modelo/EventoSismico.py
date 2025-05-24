from datetime import datetime
from Modelo.SerieTemporal import SerieTemporal
from Modelo.CambioEstado import CambioEstado

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, valorMagnitud: int, 
                 latitudHipocentro: float, longitudHipocentro: float,
                 latitudEpicentro: float, longitudEpicentro: float):
        self.fechaHoraOcurrencia = fechaHoraOcurrencia # datetime
        self.valorMagnitud = valorMagnitud # int
        self.latitudHipocentro = latitudHipocentro # float
        self.longitudHipocentro = longitudHipocentro # float
        self.latitudEpicentro = latitudEpicentro # float
        self.longitudEpicentro = longitudEpicentro # float
        self.serieTemporal = [] # puntero a objetos SerieTemporal
        self.cambiosEstado = [] # puntero a objetos CambioEstado
