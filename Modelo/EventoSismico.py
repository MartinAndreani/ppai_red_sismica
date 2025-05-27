from datetime import datetime
from Modelo.SerieTemporal import SerieTemporal
from Modelo.CambioEstado import CambioEstado
from Modelo.AlcanceSismo import AlcanceSismo
from Modelo.ClasificacionSismo import ClasificacionSismo
from Modelo.OrigenDeGeneracion import OrigenDeGeneracion

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, valorMagnitud: float, latitudHipocentro: float, longitudHipocentro: float,
                 latitudEpicentro: float, longitudEpicentro: float, alcanceSismo: AlcanceSismo, clasificacionSismo: ClasificacionSismo
                 , origenDeGeneracion: OrigenDeGeneracion):
    
        self.fechaHoraOcurrencia = fechaHoraOcurrencia # datetime
        self.valorMagnitud = valorMagnitud # float
        self.latitudHipocentro = latitudHipocentro # float
        self.longitudHipocentro = longitudHipocentro # float
        self.latitudEpicentro = latitudEpicentro # float
        self.longitudEpicentro = longitudEpicentro # float
        self.serieTemporal = [] # puntero a objetos SerieTemporal
        self.cambiosEstado = [] # puntero a objetos CambioEstado
        self.alcanceSismo = alcanceSismo  # puntero a objeto AlcanceSismo
        self.clasificacionSismo = clasificacionSismo  # puntero a objeto ClasificacionSismo
        self.origenDeGeneracion = origenDeGeneracion # puntero a objeto OrigenDeGeneracion

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
    
    def bloquearEnRevision(self, fechaHoraActual, estado):
        self.finalizarCambioEstadoActual(fechaHoraActual)
        self.crearCambioEstado(estado)


    def finalizarCambioEstadoActual(self, fechaHoraFin):
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esEstadoActual():
                cambioEstado.setFechaHoraFin(fechaHoraFin)
                break

    def crearCambioEstado(self, estado):
        fechaHoraActual = datetime.now()
        nuevoCambioEstado = CambioEstado(fechaHoraActual, None, estado)
        self.cambiosEstado.append(nuevoCambioEstado)
    
    def getAlcance(self):
        self.alcanceSismo.getNombre()

    def getClasificacion(self):
        self.clasificacionSismo.getNombre()
        self.clasificacionSismo.getKmProfundidadDesde()
        self.clasificacionSismo.getKmProfundidadHasta()

    def getOrigen(self):
        self.origenDeGeneracion.getNombre()

    def buscarDatosMuestrasSismicas(self):
        for serie in self.serieTemporal:
            serie.buscarDatosMuestrasSismicas()
