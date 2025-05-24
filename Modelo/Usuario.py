from Modelo.Empleado import Empleado

class Usuario:
    def __init__(self, empleado: Empleado, nombreUsuario: str, contrasena: str):
        self.empleado = empleado
        self.nombreUsuario = nombreUsuario
        self.contrasena = contrasena
        
    def getDatosEmpleado(self):
        return self.empleado.getDatos()
        
    def validarUsuario(self, nombreUsuario: str, contrasena: str) -> bool:
        return self.nombreUsuario == nombreUsuario and self.contrasena == contrasena
