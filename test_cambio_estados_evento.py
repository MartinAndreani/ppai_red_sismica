from datetime import datetime
from Modelo.EventoSismico import EventoSismico
from Modelo.Estado import Estado
from Modelo.CambioEstado import CambioEstado

def test_cambio_estados_evento():
    print("\n=== Test de Cambios de Estado de Evento Sísmico ===")
    
    # 1. Crear evento sísmico
    print("\n1. Creando evento sísmico...")
    evento = EventoSismico(
        fechaHoraOcurrencia=datetime(2025, 2, 21, 19, 5, 41),
        valorMagnitud=5.5,
        latitudHipocentro=-34.6037,
        longitudHipocentro=-58.3816,
        latitudEpicentro=-34.6037,
        longitudEpicentro=-58.3816
    )
    print("Evento sísmico creado")
    
    # 2. Crear estados
    print("\n2. Creando estados...")
    estado_auto_detectado = Estado("EventoSismico", "AutoDetectado")
    estado_bloqueado = Estado("EventoSismico", "BloqueadoEnRevision")
    estado_rechazado = Estado("EventoSismico", "Rechazado")
    print("Estados creados")
    
    # 3. Crear y agregar estado inicial (AutoDetectado)
    print("\n3. Configurando estado inicial (AutoDetectado)...")
    cambio_estado_inicial = CambioEstado(
        fechaHoraInicio=datetime.now(),
        fechaHoraFin=None,
        estado=estado_auto_detectado
    )
    evento.agregarCambioEstado(cambio_estado_inicial)
    print("Estado inicial configurado")
    
    # 4. Verificar estado inicial
    print("\n4. Verificando estado inicial...")
    print(f"¿Es AutoDetectado? {evento.esAutoDetectado()}")
    
    # 5. Bloquear en revisión
    print("\n5. Bloqueando evento en revisión...")
    fecha_bloqueo = datetime.now()
    evento.bloquearEnRevision(fecha_bloqueo, estado_bloqueado)
    print("Evento bloqueado en revisión")
    
    # 6. Verificar estado después del bloqueo
    print("\n6. Verificando estado después del bloqueo...")
    print(f"¿Es AutoDetectado? {evento.esAutoDetectado()}")
    
    # 7. Rechazar evento
    print("\n7. Rechazando evento...")
    fecha_rechazo = datetime.now()
    evento.rechazar(fecha_rechazo, estado_rechazado)
    print("Evento rechazado")
    
    # 8. Verificar cambios de estado finales
    print("\n8. Verificando cambios de estado finales...")
    for i, cambio in enumerate(evento.cambiosEstado, 1):
        print(f"\nCambio de estado {i}:")
        print(f"Estado: {cambio.estado.nombre}")
        print(f"Fecha inicio: {cambio.fechaHoraInicio}")
        print(f"Fecha fin: {cambio.fechaHoraFin}")
        print(f"¿Es estado actual? {cambio.esEstadoActual()}")

    print("\nTest finalizado correctamente. La secuencia de cambios de estado fue verificada.")

if __name__ == "__main__":
    test_cambio_estados_evento() 