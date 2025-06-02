from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual
class PantallaRegistrarResultadoDeRevisiónManual:
    def __init__(self):
        self.gestor = GestorRegistrarResultadoDeRevisionManual()
        self.datosRestantes = []
        self.eventos_ordenados = []

    def habilitar(self, eventos):
        self.gestor.listaEventosSimicosNoRevisados = []
        self.gestor.listaDatosPrincipalesDeEventos = []
        self.gestor.buscarEventosSimicosNoRevisados(eventos)
        self.gestor.buscarDatosPrincipalesEventosSismicosNoRevisados()
        self.gestor.ordenarDatosDeEventosSismicosPorFechaHoraOcurrencia()
        self.eventos_ordenados = self.gestor.listaDatosPrincipalesDeEventos
        return self.eventos_ordenados or []
    
    def seleccionarEventoSismico(self, id_evento, lista_estados):
        self.gestor.tomarSeleccionEventoSismico(id_evento, lista_estados)

    def mostrarDatosEventoSismico(self):
        return self.gestor.listaDatosRestantesDeEventoSeleccionado
    def mostrarSeriesTemporales(self):
        self.gestor.buscarDatosSeriesTemporales() 
        self.gestor.ordenarSeriesTemporalesPorEstacionSismologica() 
        self.series_temporales = self.gestor.seriesTemporalesDeEventoSeleccionado
        return self.series_temporales 
    def habilitarVisualizacionMapa():
       pass
    def solicitarOpcionModificacion():
        pass
    def seleccionarResultadoRevisionManual(self, resultado, lista_estados):
        self.gestor.resultadoDeRevisionManual = resultado
        self.gestor.tomarResultadoDeRevisionManual(lista_estados)

    def getDatosRestantes(self):
    # Devuelve los datos reales del gestor
        return self.gestor.listaDatosRestantesDeEventoSeleccionado
