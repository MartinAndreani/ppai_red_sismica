from Modelo.Usuario import Usuario

class Sesion:
    def __init__(self):
        self.usuario = None # puntero a objeto Usuario
        self.fechaHoraInicio = None # datetime
        self.fechaHoraFin = None # datetime
        
    def setUsuario(self, usuario):
        self.usuario = usuario
        
    def getDatosASLogueado(self):
        return self.usuario.getDatosEmpleado()
        
    def validarSesion(self, nombreUsuario: str, contrasena: str) -> bool:
        return self.usuario.validarUsuario(nombreUsuario, contrasena)