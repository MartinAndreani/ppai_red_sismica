class TipoDeDato:
    def __init__(self, denominacion: str, valorUmbral: float, nombreUnidadMedida :str):
        self.valorUmbral = valorUmbral # float
        self.denominacion = denominacion # str
        self.nombreUnidadMedida = nombreUnidadMedida # str

    def getDenominacion(self):
        return self.denominacion
    
    def getNombreUnidadMedida(self):
        return self.nombreUnidadMedida
    
    def getValorUmbral(self):
        return self.valorUmbral
        
        
        
        
