from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual
class PantallaRegistrarResultadoDeRevisiónManual:
    def habilitar(self, eventos):
        gestor = GestorRegistrarResultadoDeRevisionManual()
        datos = gestor.buscarEventosSimicosNoRevisados(eventos)
        lista = gestor.buscarDatosPrincipalesEventosSismicosNoRevisados(datos)
        lista_ordenada = gestor.ordenarDatosDeEventosSismicosPorFechaHoraOcurrencia(lista)
        if lista_ordenada is None:
            lista_ordenada = []
        for evento in lista_ordenada:
            if 'fechaHora' in evento and hasattr(evento['fechaHora'], 'isoformat'):
                evento['fechaHora'] = evento['fechaHora'].isoformat()
        return lista_ordenada
    def solicitarSeleccionDeEventoSismico(self):
        # eventos = GestorRegistrarResultadoDeRevisionManual().ordenarDatosDeEventosSismicosPorFechaHoraOcurrencia()
        pass
    def seleccionarEventoSismico(self):
        pass
    def mostrarDatosEventoSismico(self):
        pass
    def habilitarVisualizacionMapa():
       pass
    def solicitarOpcionModificacion():
        pass
    