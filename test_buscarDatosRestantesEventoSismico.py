from datetime import datetime
from Modelo.EventoSismico import EventoSismico
from Modelo.AlcanceSismo import AlcanceSismo
from Modelo.ClasificacionSismo import ClasificacionSismo
from Modelo.OrigenDeGeneracion import OrigenDeGeneracion
from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual

# Crear objetos necesarios
alcance = AlcanceSismo("Local")
clasificacion = ClasificacionSismo("Superficial", 0, 70)
origen = OrigenDeGeneracion("Tectónico")

# Crear evento sísmico
evento = EventoSismico(
    fechaHoraOcurrencia=datetime(2025, 2, 21, 19, 5, 41),
    valorMagnitud=5.5,
    latitudHipocentro=-34.6037,
    longitudHipocentro=-58.3816,
    latitudEpicentro=-34.6037,
    longitudEpicentro=-58.3816
)
evento.setAlcanceSismo(alcance)
evento.setClasificacionSismo(clasificacion)
evento.setOrigenDeGeneracion(origen)

# Crear gestor y ejecutar
gestor = GestorRegistrarResultadoDeRevisionManual()
gestor.eventoSismicoSeleccionado = evento
gestor.buscarDatosRestantesEventoSismico()

# Mostrar resultados
print("\nDatos restantes del evento sísmico:")
for datos in gestor.listaDatosRestantesDeEventos:
    print(f"\nAlcance: {datos['alcance']}")
    print(f"Clasificación: {datos['clasificacion']['nombre']}")
    print(f"  Profundidad desde: {datos['clasificacion']['profundidadDesde']} km")
    print(f"  Profundidad hasta: {datos['clasificacion']['profundidadHasta']} km")
    print(f"Origen: {datos['origen']}") 