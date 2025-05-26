from Modelo.SerieTemporal import SerieTemporal

class Sismografo:
    def __init__(self, nombre: str, ubicacion: str):
        self.identificadorSismografo = None # str
        self.serieTemporal = [] # puntero a objetos SerieTemporal

