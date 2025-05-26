from datetime import datetime
from typing import List
from Modelo.EventoSismico import EventoSismico
from Modelo.Estado import Estado

class GestorRegistrarResultadoDeRevisionManual:
    def __init__(self):
        self.listaEventosSimicosNoRevisados = []  # Lista de punteros a objetos EventoSismico
        self.listaDatosPrincipalesDeEventos = [] # Lista con atributos de Eventos Sismicos
        self.estadoBloqueadoEnRevision = None     # Puntero a objeto Estado
        self.eventoSismicoSeleccionado = None     # Puntero a objeto EventoSismico
        self.aprobacionVisualizacionMapa = False  # bool
        self.resultadoDeRevisionManual = None     # Confirmar evento, Rechazar evento o Solicitar revisión a experto
        self.estadoRechazado = None              # Puntero a objeto Estado
        self.datosUsuarioLogueado = []           # Lista de strings
        
    def buscarEventosSimicosNoRevisados(self, eventos):
        for evento in eventos:
            if evento.esAutoDetectado():
                self.listaEventosSimicosNoRevisados.append(evento)

    def buscarDatosPrincipalesEventosSismicosNoRevisados(self):
        for evento in self.listaEventosSimicosNoRevisados:
            datosEvento = {
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

    def tomarSeleccionEventoSismico(self):
        pass

    def buscarEstadoBloqueadoEnRevision(self, estados):
        for estado in estados:
            if estado.esAmbitoDeEventoSismico() and estado.esBloqueadoEnRevision():
                self.estadoBloqueadoEnRevision = estado
                break

    def getFechaHoraActual(self):
        return datetime.now()

    def bloquearEventoSismicoSeleccionado(self):
        fechaHoraActual = self.getFechaHoraActual()
        self.eventoSismicoSeleccionado.finalizarCambioEstadoActual(fechaHoraActual)


    def buscarDatosRestantesEventoSismico(self):
        pass

    def buscarDatosMuestrasSismicasDeEventoSismico(self):
        pass

    def buscarNombreEstacionSismologicaDeCadaSerieTemporal(self):
        pass

    def ordenarInstantesDeTiempoPorEstacionSismologica(self):
        pass

    def tomarAprobacionVisualizacionMapaEventoSismico(self):
        pass

    def tomarCambioDatosModificablesDeEventoSismico(self):
        pass

    def tomarResultadoDeRevisionManual(self):
        pass

    def validarDatosModificablesYResultadoDeRevisionManual(self):
        pass

    def buscarEstadoRechazado(self, estados):
        for estado in estados:
            if estado.esAmbitoDeEventoSismico() and estado.esRechazado():
                self.estadoRechazado = estado
                break

    def buscarDatosASLogueado(self):
        pass

    def finCU(self):
        pass 
