class Estado:
    def __init__(self, ambito: str, nombre: str):
        self.ambito = ambito # str
        self.nombre = nombre # str

    def esAutoDetectado(self):
        return self.nombre == "AutoDetectado"
    
    def esAmbitoDeEventoSismico(self):
        return self.ambito == "EventoSismico"
    
    def esBloqueadoEnRevision(self):
        return self.nombre == "BloqueadoEnRevision"
    
    def esRechazado(self):
        return self.nombre == "Rechazado"
    
    