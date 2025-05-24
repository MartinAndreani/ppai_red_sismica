from datetime import datetime
from typing import List
from Modelo.EventoSismico import EventoSismico
from Modelo.Estado import Estado

class GestorRegistrarResultadoDeRevisionManual:
    def __init__(self):
        self.listaEventosSimicosNoRevisados: List[EventoSismico] = []  # Lista de punteros a objetos EventoSismico
        self.estadoBloqueadoEnRevision: Estado = None     # Puntero a objeto Estado
        self.eventoSismicoSeleccionado: EventoSismico = None     # Puntero a objeto EventoSismico
        self.aprobacionVisualizacionMapa: bool = False  # bool
        self.resultadoDeRevisionManual = None     # Confirmar evento, Rechazar evento o Solicitar revisión a experto
        self.estadoRechazado: Estado = None              # Puntero a objeto Estado
        self.datosUsuarioLogueado: List[str] = []           # Lista de strings

    def obtenerFechaHoraActual(self):
        return datetime.now()
        
