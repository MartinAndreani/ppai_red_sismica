class Empleado:
    def __init__(self, nombre:str, apellido: str, mail: str, numero: str):
        self.nombre = nombre # str
        self.apellido = apellido # str
        self.mail = mail # str
        self.numero = numero # str
        
    def getDatos(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'mail': self.mail,
            'numero': self.numero
        }
        
        
        
        