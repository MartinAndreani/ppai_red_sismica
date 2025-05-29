from Modelo.Usuario import Usuario

class Sesion: # Singleton, se mantiene una única instancia de Sesion que se comparte en toda la app
    _instancia = None
    
    def __new__(cls): # Asegura que se cree una sola instancia 
        if cls._instancia is None:
            cls._instancia = super(Sesion, cls).__new__(cls)
            cls._instancia.usuario = None
            cls._instancia.fechaHoraInicio = None
            cls._instancia.fechaHoraFin = None
        return cls._instancia
    
    @classmethod
    def getSesionActual(cls): # Si no existe una instancia crea una nueva
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
        
    def setUsuario(self, usuario):
        self.usuario = usuario
        
    def getDatosASLogueado(self):
        return self.usuario.getDatosEmpleado()
        
    def validarSesion(self, nombreUsuario: str, contrasena: str) -> bool:
        return self.usuario.validarUsuario(nombreUsuario, contrasena)