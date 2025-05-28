class ClasificacionSismo:
    def __init__(self, nombre: str, kmProfundidadDesde: float, kmProfundidadHasta: float):
        self.nombre = nombre # str
        self.kmProfundidadDesde = kmProfundidadDesde # float
        self.kmProfundidadHasta = kmProfundidadHasta # float

    def getNombre(self):
        return self.nombre
    
    def getKmProfundidadDesde(self):
        return self.kmProfundidadDesde
    
    def getKmProfundidadHasta(self):
        return self.kmProfundidadHasta
    
    