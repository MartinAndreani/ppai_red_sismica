from datetime import datetime

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, valorMagnitud: int, 
                 latitudHipocentro: float, longitudHipocentro: float,
                 latitudEpicentro: float, longitudEpicentro: float):
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.valorMagnitud = valorMagnitud
        self.latitudHipocentro = latitudHipocentro
        self.longitudHipocentro = longitudHipocentro
        self.latitudEpicentro = latitudEpicentro
        self.longitudEpicentro = longitudEpicentro

