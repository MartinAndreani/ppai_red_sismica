from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual
class PantallaRegistrarResultadoDeRevisiónManual:
    def habilitar(self, eventos):
        self.datosRestantes = [...]
        self.gestor = GestorRegistrarResultadoDeRevisionManual()
        self.gestor.buscarEventosSimicosNoRevisados(eventos)
        self.gestor.buscarDatosPrincipalesEventosSismicosNoRevisados()
        self.gestor.ordenarDatosDeEventosSismicosPorFechaHoraOcurrencia()
        self.eventos_ordenados = self.gestor.listaDatosPrincipalesDeEventos

        for evento in self.eventos_ordenados:
            if 'fechaHora' in evento and hasattr(evento['fechaHora'], 'isoformat'):
                evento['fechaHora'] = evento['fechaHora'].isoformat()
        return self.eventos_ordenados or []
    def seleccionarEventoSismico(self, id_evento):
        # Buscamos el objeto EventoSismico original con el id
        for evento in self.gestor.listaEventosSimicosNoRevisados:
            if evento.getId() == id_evento:
                self.gestor.tomarSeleccionEventoSismico(evento)
                break

    def mostrarDatosEventoSismico(self):
        return self.gestor.listaDatosRestantesDeEventoSeleccionado
    def habilitarVisualizacionMapa():
       pass
    def solicitarOpcionModificacion():
        pass
    def getDatosRestantes(self):
    # Devuelve los datos reales del gestor
        return self.gestor.listaDatosRestantesDeEventoSeleccionado