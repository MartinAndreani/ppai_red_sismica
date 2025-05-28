from Modelo.TipoDeDato import TipoDeDato

class DetalleMuestraSismica:
    def __init__(self, valor: float):
        self.valor = valor # float
        self.tipoDeDato = None # puntero a objeto TipoDeDato

    def setTipoDeDato(self, tipoDeDato):
        self.tipoDeDato = tipoDeDato

    def getDatos(self):
        return {
            'valor': self.valor,
            'denominacion': self.tipoDeDato.getDenominacion(),
            'unidadMedida': self.tipoDeDato.getNombreUnidadMedida(),
            'valorUmbral': self.tipoDeDato.getValorUmbral()
        }
