from Modelo.Usuario import Usuario

class Sesion:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario # puntero a objeto Usuario
        self.fechaHoraInicio = None # datetime
        self.fechaHoraFin = None # datetime
        
    def getDatosASLogueado(self):
        return self.usuario.getDatosEmpleado()
        
    def validarSesion(self, nombreUsuario: str, contrasena: str) -> bool:
        return self.usuario.validarUsuario(nombreUsuario, contrasena)