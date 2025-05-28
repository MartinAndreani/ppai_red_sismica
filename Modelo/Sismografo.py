class Sismografo:
    def __init__(self, identificadorSismografo: str):
        self.identificadorSismografo = identificadorSismografo # str
        self.estacionSismologica = None # puntero a objeto EstacionSismologica
        
    def setEstacionSismologica(self, estacionSismologica):
        self.estacionSismologica = estacionSismologica # puntero a objeto EstacionSismologica
        
    def getNombreEstacionSismologica(self):
        return self.estacionSismologica.getNombre()

