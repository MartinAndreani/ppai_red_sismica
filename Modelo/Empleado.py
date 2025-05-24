class Empleado:
    def __init__(self, nombre:str, apellido: str, mail: str, numero: str):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.numero = numero
        
    def getDatos(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'mail': self.mail,
            'numero': self.numero
        }
        
        
        
        