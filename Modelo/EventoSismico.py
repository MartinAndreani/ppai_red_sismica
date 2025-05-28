from datetime import datetime
from Modelo.SerieTemporal import SerieTemporal
from Modelo.CambioEstado import CambioEstado
from Modelo.AlcanceSismo import AlcanceSismo
from Modelo.ClasificacionSismo import ClasificacionSismo
from Modelo.OrigenDeGeneracion import OrigenDeGeneracion

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, valorMagnitud: float, latitudHipocentro: float, longitudHipocentro: float,
                 latitudEpicentro: float, longitudEpicentro: float):
        self.fechaHoraOcurrencia = fechaHoraOcurrencia # datetime
        self.valorMagnitud = valorMagnitud # float
        self.latitudHipocentro = latitudHipocentro # float
        self.longitudHipocentro = longitudHipocentro # float
        self.latitudEpicentro = latitudEpicentro # float
        self.longitudEpicentro = longitudEpicentro # float
        self.serieTemporal = [] # lista de punteros a objetos SerieTemporal
        self.cambiosEstado = [] # lista de punteros a objetos CambioEstado
        self.alcanceSismo = None # puntero a objeto AlcanceSismo
        self.clasificacionSismo = None # puntero a objeto ClasificacionSismo
        self.origenDeGeneracion = None # puntero a objeto OrigenDeGeneracion

    def setAlcanceSismo(self, alcanceSismo):
        self.alcanceSismo = alcanceSismo

    def setClasificacionSismo(self, clasificacionSismo):
        self.clasificacionSismo = clasificacionSismo

    def setOrigenDeGeneracion(self, origenDeGeneracion):
        self.origenDeGeneracion = origenDeGeneracion

    def agregarSerieTemporal(self, serieTemporal):
        self.serieTemporal.append(serieTemporal)

    def agregarCambioEstado(self, cambioEstado):
        self.cambiosEstado.append(cambioEstado)

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
        return self.alcanceSismo.getNombre()

    def getClasificacion(self):
        return {
            'nombre': self.clasificacionSismo.getNombre(),
            'profundidadDesde': self.clasificacionSismo.getKmProfundidadDesde(),
            'profundidadHasta': self.clasificacionSismo.getKmProfundidadHasta()
        }

    def getOrigen(self):
        return self.origenDeGeneracion.getNombre()

    def buscarDatosSeriesTemporales(self):
        datos_series = []
        for serie in self.serieTemporal:
            datos_serie = serie.getDatos()
            # Agregar nombre de estación sismológica usando la cadena de mensajes
            datos_serie['estacionSismologica'] = serie.getNombreEstacionSismologica()
            datos_series.append(datos_serie)
        return datos_series
