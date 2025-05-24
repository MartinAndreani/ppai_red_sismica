from Modelo.TipoDeDato import TipoDeDato

class DetalleMuestraSismica:
    def __init__(self, valor: float, tipoDeDato: TipoDeDato):
        self.valor = valor # float
        self.tipoDeDato = tipoDeDato # puntero a objeto TipoDeDato

