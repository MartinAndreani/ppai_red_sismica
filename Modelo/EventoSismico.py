from datetime import datetime
from Modelo.SerieTemporal import SerieTemporal
from Modelo.CambioEstado import CambioEstado

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, valorMagnitud: float, 
                 latitudHipocentro: float, longitudHipocentro: float,
                 latitudEpicentro: float, longitudEpicentro: float):
        self.fechaHoraOcurrencia = fechaHoraOcurrencia # datetime
        self.valorMagnitud = valorMagnitud # float
        self.latitudHipocentro = latitudHipocentro # float
        self.longitudHipocentro = longitudHipocentro # float
        self.latitudEpicentro = latitudEpicentro # float
        self.longitudEpicentro = longitudEpicentro # float
        self.serieTemporal = [] # puntero a objetos SerieTemporal
        self.cambiosEstado = [] # puntero a objetos CambioEstado

    def esAutoDetectado(self):
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esEstadoActual():
                return cambioEstado.esAutoDetectado()
        return False

    def getFechaHoraOcurrencia(self):
        return self.fechaHoraOcurrencia

    def getValorMagnitud(self):
        return self.valorMagnitud

    def getLatitudHipocentro(self):
        return self.latitudHipocentro

    def getLongitudHipocentro(self):
        return self.longitudHipocentro

    def getLatitudEpicentro(self):
        return self.latitudEpicentro

    def getLongitudEpicentro(self):
        return self.longitudEpicentro
    
    def finalizarCambioEstadoActual(self, fechaHoraFin):
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esEstadoActual():
                cambioEstado.setFechaHoraFin(fechaHoraFin)
                break

    def crearCambioEstado(self, estado):
        fechaHoraActual = datetime.now()
        nuevoCambioEstado = CambioEstado(fechaHoraActual, None, estado)
        self.cambiosEstado.append(nuevoCambioEstado)
            