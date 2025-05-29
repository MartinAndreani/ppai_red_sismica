from datetime import datetime
from Modelo.Sesion import Sesion
from Modelo.Usuario import Usuario
from Modelo.Empleado import Empleado

def test_sesion_singleton():
    print("\n1. Creando primera instancia de Sesion...")
    sesion1 = Sesion()
    print("Primera instancia creada")
    
    print("\n2. Creando segunda instancia de Sesion...")
    sesion2 = Sesion()
    print("Segunda instancia creada")
    
    print("\n3. Verificando que ambas instancias son la misma...")
    print(f"¿Son la misma instancia? {sesion1 is sesion2}")
    
    print("\n4. Obteniendo sesión actual...")
    sesion_actual = Sesion.getSesionActual()
    print(f"¿Es la misma instancia? {sesion_actual is sesion1}")

def test_datos_usuario():
    print("\n1. Creando empleado...")
    empleado = Empleado("Juan", "Pérez", "juan.perez@utn.edu.ar", "123456789")
    print(f"Empleado creado: {empleado.getDatos()}")
    
    print("\n2. Creando usuario...")
    usuario = Usuario("jperez", "password123")
    usuario.setEmpleado(empleado)
    print("Usuario creado y vinculado con empleado")
    
    print("\n3. Configurando sesión...")
    sesion = Sesion.getSesionActual()
    sesion.setUsuario(usuario)
    print("Usuario configurado en sesión")
    
    print("\n4. Obteniendo datos del usuario logueado...")
    datos_usuario = sesion.getDatosASLogueado()
    print(f"Datos del usuario logueado: {datos_usuario}")

if __name__ == "__main__":
    print("=== Test de Patrón Singleton de Sesión ===")
    test_sesion_singleton()
    
    print("\n=== Test de Datos de Usuario Logueado ===")
    test_datos_usuario() 