from Modelo.Empleado import Empleado

class Usuario:
    def __init__(self, empleado: Empleado, nombreUsuario: str, contrasena: str):
        self.empleado = empleado # puntero a objeto Empleado
        self.nombreUsuario = nombreUsuario # str
        self.contrasena = contrasena # str
        
    def getDatosEmpleado(self):
        return self.empleado.getDatos()
        
    def validarUsuario(self, nombreUsuario: str, contrasena: str) -> bool:
        return self.nombreUsuario == nombreUsuario and self.contrasena == contrasena
