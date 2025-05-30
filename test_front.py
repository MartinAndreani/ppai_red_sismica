from datetime import datetime, timedelta
from Modelo.EventoSismico import EventoSismico
from Modelo.AlcanceSismo import AlcanceSismo
from Modelo.ClasificacionSismo import ClasificacionSismo
from Modelo.OrigenDeGeneracion import OrigenDeGeneracion
from Modelo.TipoDeDato import TipoDeDato
from Modelo.DetalleMuestraSismica import DetalleMuestraSismica
from Modelo.MuestraSismica import MuestraSismica
from Modelo.SerieTemporal import SerieTemporal
from Modelo.Sismografo import Sismografo
from Modelo.EstacionSismologica import EstacionSismologica
from Modelo.Estado import Estado
from Modelo.CambioEstado import CambioEstado
# List to hold the generated seismic events
eventos = []

# Global counters for IDs
_event_id_counter = 100
_sismografo_id_counter = 1
_estacion_id_counter = 1

def generar_evento_sismico(
    valor_magnitud,
    lat_hipocentro,
    lon_hipocentro,
    lat_epicentro,
    lon_epicentro,
    alcance_nombre,
    clasificacion_nombre,
    prof_desde,
    prof_hasta,
    origen_nombre,
    fecha_base,
    num_estaciones=3
):
    global _event_id_counter, _sismografo_id_counter, _estacion_id_counter
    
    # Crear tipos de datos (pueden ser comunes para todos los eventos)
    tipo_velocidad = TipoDeDato("Velocidad de onda", 5.0, "Km/seg")
    tipo_frecuencia = TipoDeDato("Frecuencia de onda", 8.0, "Hz")
    tipo_longitud = TipoDeDato("Longitud", 0.5, "km/ciclo")

    # Crear objetos necesarios
    alcance = AlcanceSismo(alcance_nombre)
    clasificacion = ClasificacionSismo(clasificacion_nombre, prof_desde, prof_hasta)
    origen = OrigenDeGeneracion(origen_nombre)

    evento = EventoSismico(
        fechaHoraOcurrencia=fecha_base,
        valorMagnitud=valor_magnitud,
        latitudHipocentro=lat_hipocentro,
        longitudHipocentro=lon_hipocentro,
        latitudEpicentro=lat_epicentro,
        longitudEpicentro=lon_epicentro
    )
    evento.setAlcanceSismo(alcance)
    evento.setClasificacionSismo(clasificacion)
    evento.setOrigenDeGeneracion(origen)

    # --- AGREGAR ESTADO AutoDetectado ---
    estado_auto = Estado("EventoSismico", "AutoDetectado")
    cambio_estado = CambioEstado(
        fechaHoraInicio=fecha_base,
        fechaHoraFin=None,
        estado=estado_auto
    )
    evento.agregarCambioEstado(cambio_estado)
    # --- FIN AGREGAR ESTADO ---

    # Generar series temporales dinámicamente
    estaciones_creadas = []
    for i in range(num_estaciones):
        estacion_nombre = f"Estación {chr(65 + _estacion_id_counter % 26)}" # A, B, C...
        estacion = EstacionSismologica(estacion_nombre)
        _estacion_id_counter += 1
        
        sismografo_nombre = f"SISM{_sismografo_id_counter:03d}"
        sismografo = Sismografo(sismografo_nombre)
        sismografo.setEstacionSismologica(estacion)
        _sismografo_id_counter += 1

        serie = SerieTemporal(
            condicionAlarma=False,
            fechaHoraInicioMuestras=fecha_base,
            frecuenciaMuestreo="50 Hz"
        )
        serie.setSismografo(sismografo)

        # Crear muestras sísmicas para la serie
        def crear_muestra(fecha, velocidad, frecuencia, longitud):
            muestra = MuestraSismica(fecha)
            detalle1 = DetalleMuestraSismica(velocidad)
            detalle1.setTipoDeDato(tipo_velocidad)
            detalle2 = DetalleMuestraSismica(frecuencia)
            detalle2.setTipoDeDato(tipo_frecuencia)
            detalle3 = DetalleMuestraSismica(longitud)
            detalle3.setTipoDeDato(tipo_longitud)
            muestra.detalles = [detalle1, detalle2, detalle3]
            return muestra

        # Generar muestras con ligeras variaciones
        serie.muestras = [
            crear_muestra(fecha_base + timedelta(minutes=0), 7.0 + i*0.01, 10.0 + i*0.01, 0.7 + i*0.005),
            crear_muestra(fecha_base + timedelta(minutes=5), 7.02 + i*0.01, 10.0 + i*0.01, 0.69 + i*0.005)
        ]
        evento.agregarSerieTemporal(serie)
    
    return evento

# --- Generar 5 eventos sísmicos ---

# Evento 1
eventos.append(generar_evento_sismico(
    valor_magnitud=5.5,
    lat_hipocentro=-34.6037,
    lon_hipocentro=-58.3816,
    lat_epicentro=-34.6037,
    lon_epicentro=-58.3816,
    alcance_nombre="Local",
    clasificacion_nombre="Superficial",
    prof_desde=0,
    prof_hasta=70,
    origen_nombre="Tectónico",
    fecha_base=datetime(2025, 2, 21, 19, 5, 41),
    num_estaciones=3
))

# Evento 2
eventos.append(generar_evento_sismico(
    valor_magnitud=6.1,
    lat_hipocentro=-33.00,
    lon_hipocentro=-70.00,
    lat_epicentro=-33.00,
    lon_epicentro=-70.00,
    alcance_nombre="Regional",
    clasificacion_nombre="Intermedio",
    prof_desde=71,
    prof_hasta=300,
    origen_nombre="Volcánico",
    fecha_base=datetime(2025, 3, 10, 10, 30, 0),
    num_estaciones=2
))

# Evento 3
eventos.append(generar_evento_sismico(
    valor_magnitud=4.8,
    lat_hipocentro=-25.00,
    lon_hipocentro=-65.00,
    lat_epicentro=-25.00,
    lon_epicentro=-65.00,
    alcance_nombre="Local",
    clasificacion_nombre="Superficial",
    prof_desde=0,
    prof_hasta=70,
    origen_nombre="Antrópico",
    fecha_base=datetime(2025, 4, 1, 14, 0, 0),
    num_estaciones=4
))

# Evento 4
eventos.append(generar_evento_sismico(
    valor_magnitud=7.0,
    lat_hipocentro=-40.00,
    lon_hipocentro=-72.00,
    lat_epicentro=-40.00,
    lon_epicentro=-72.00,
    alcance_nombre="Nacional",
    clasificacion_nombre="Profundo",
    prof_desde=301,
    prof_hasta=700,
    origen_nombre="Tectónico",
    fecha_base=datetime(2025, 5, 5, 23, 15, 0),
    num_estaciones=3
))

# Evento 5
eventos.append(generar_evento_sismico(
    valor_magnitud=5.2,
    lat_hipocentro=-30.00,
    lon_hipocentro=-60.00,
    lat_epicentro=-30.00,
    lon_epicentro=-60.00,
    alcance_nombre="Local",
    clasificacion_nombre="Superficial",
    prof_desde=0,
    prof_hasta=70,
    origen_nombre="Tectónico",
    fecha_base=datetime(2025, 5, 20, 8, 45, 0),
    num_estaciones=2
))

# Opcional: imprimir los IDs de los eventos generados para verificar
# for ev in eventos:
#     print(f"Evento ID: {ev.getId()}, Fecha: {ev.getFechaHoraOcurrencia()}")