from datetime import datetime
from typing import List
from Modelo.EventoSismico import EventoSismico
from Modelo.Estado import Estado
from Controlador.GestorGenerarSismograma import GestorGenerarSismograma
from Modelo.Sesion import Sesion

class GestorRegistrarResultadoDeRevisionManual:
    def __init__(self):
        self.listaEventosSimicosNoRevisados = []  # Lista de punteros a objetos EventoSismico
        self.listaDatosPrincipalesDeEventos = [] # Lista con atributos de Eventos Sismicos
        self.estadoBloqueadoEnRevision = None     # Puntero a objeto Estado
        self.eventoSismicoSeleccionado = None     # Puntero a objeto EventoSismico
        self.listaDatosRestantesDeEventoSeleccionado = []   # Lista con datos del evento sísmico (alcance, clasificación, origen)
        self.seriesTemporalesDeEventoSeleccionado = []       # Lista de series temporales con sus datos para generar sismogramas
        self.aprobacionVisualizacionMapa = False  # bool
        self.aprobacionModificacionDatos = False  # bool
        self.resultadoDeRevisionManual = None     # Confirmar evento, Rechazar evento o Solicitar revisión a experto
        self.estadoRechazado = None  # Puntero a objeto estado Rechazado
        self.datosUsuarioLogueado = []   # Lista de strings
        
    def buscarEventosSimicosNoRevisados(self, eventos):
        for evento in eventos:
            if evento.esAutoDetectado():
                self.listaEventosSimicosNoRevisados.append(evento)

    def buscarDatosPrincipalesEventosSismicosNoRevisados(self):
        for evento in self.listaEventosSimicosNoRevisados:
            datosEvento = {
                'id': evento.getId(),
                'fechaHora': evento.getFechaHoraOcurrencia(),
                'magnitud': evento.getValorMagnitud(),
                'latitudHipocentro': evento.getLatitudHipocentro(),
                'longitudHipocentro': evento.getLongitudHipocentro(),
                'latitudEpicentro': evento.getLatitudEpicentro(),
                'longitudEpicentro': evento.getLongitudEpicentro()
            }
            self.listaDatosPrincipalesDeEventos.append(datosEvento)

    def ordenarDatosDeEventosSismicosPorFechaHoraOcurrencia(self):
        self.listaDatosPrincipalesDeEventos.sort(key=lambda x: x['fechaHora'])

    def tomarSeleccionEventoSismico(self, id_evento):
        for evento in self.listaEventosSimicosNoRevisados:
            if evento.getId() == id_evento:
                self.eventoSismicoSeleccionado = evento
                break

        if self.eventoSismicoSeleccionado:
            if self.estadoBloqueadoEnRevision is None:
                self.estadoBloqueadoEnRevision = Estado("EventoSismico", "BloqueadoEnRevision")
            self.bloquearEventoSismicoSeleccionado()
            self.buscarDatosRestantesEventoSismico()
            self.buscarDatosSeriesTemporales()

    def buscarEstadoBloqueadoEnRevision(self, estados):
        for estado in estados:
            if estado.esAmbitoDeEventoSismico() and estado.esBloqueadoEnRevision():
                self.estadoBloqueadoEnRevision = estado
                break

    def getFechaHoraActual(self):
        return datetime.now()

    def bloquearEventoSismicoSeleccionado(self):
        fechaHoraActual = self.getFechaHoraActual()
        self.eventoSismicoSeleccionado.bloquearEnRevision(fechaHoraActual, self.estadoBloqueadoEnRevision)

    def buscarDatosRestantesEventoSismico(self):
        datosRestantes = {
            'alcance': self.eventoSismicoSeleccionado.getAlcance(),
            'clasificacion': self.eventoSismicoSeleccionado.getClasificacion(),
            'origen': self.eventoSismicoSeleccionado.getOrigen()
        }
        self.listaDatosRestantesDeEventoSeleccionado.append(datosRestantes)

    def buscarDatosSeriesTemporales(self):
        # Obtener y guardar las series temporales en el atributo dedicado
        self.seriesTemporalesDeEventoSeleccionado = self.eventoSismicoSeleccionado.buscarDatosSeriesTemporales()

    def ordenarSeriesTemporalesPorEstacionSismologica(self):
        # Ordenar las series temporales por nombre de estación sismológica
        self.seriesTemporalesDeEventoSeleccionado = sorted(self.seriesTemporalesDeEventoSeleccionado, key=lambda x: x['estacionSismologica'])

    def llamarCUGenerarSismograma(self):
        GestorGenerarSismograma().generarSismogramasPorEstacion(self.seriesTemporalesDeEventoSeleccionado)
    
    def tomarAprobacionVisualizacionMapaEventoSismico(self):
        pass

    def tomarCambioDatosModificablesDeEventoSismico(self):
        pass

    def tomarResultadoDeRevisionManual(self):
        if self.resultadoDeRevisionManual == "Rechazar evento":
            self.rechazarEventoSismicoSeleccionado()
        elif self.resultadoDeRevisionManual == "Confirmar evento":
            # Aquí podrías implementar la lógica para confirmar el evento
            pass
        elif self.resultadoDeRevisionManual == "Solicitar revisión a experto":
            # Aquí podrías implementar la lógica para solicitar revisión a experto
            pass

    def validarDatosModificablesYResultadoDeRevisionManual(self): # Valida que el EventoSismico seleccionado cuente con los atributos magnitud
      
        if self.eventoSismicoSeleccionado is None:
            return False
            
        if self.eventoSismicoSeleccionado.getValorMagnitud() is None:
            return False
            
        alcance = self.eventoSismicoSeleccionado.getAlcance()
        if alcance is None or alcance == "":
            return False
            
        # Verificar que existe origen de generación (debe ser un string no vacío)
        origen = self.eventoSismicoSeleccionado.getOrigen()
        if origen is None or origen == "":
            return False
            
        # Verificar que existe un resultado de revisión manual (debe ser uno de los valores esperados)
        if self.resultadoDeRevisionManual not in ["Confirmar evento", "Rechazar evento", "Solicitar revisión a experto"]:
            return False
            
        return True

    def buscarEstadoRechazado(self, estados):
        for estado in estados:
            if estado.esAmbitoDeEventoSismico() and estado.esRechazado():
                self.estadoRechazado = estado
                break

    def buscarDatosASLogueado(self):
        sesion = Sesion.getSesionActual()
        self.datosUsuarioLogueado = sesion.getDatosASLogueado()

    def rechazarEventoSismicoSeleccionado(self):
        fechaHoraActual = self.getFechaHoraActual()
        if self.estadoRechazado is None:
            self.estadoRechazado = Estado("EventoSismico", "Rechazado")
        self.eventoSismicoSeleccionado.rechazar(fechaHoraActual, self.estadoRechazado)

    def finCU(self):
        pass 