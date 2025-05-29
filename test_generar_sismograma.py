from datetime import datetime
from Modelo.TipoDeDato import TipoDeDato
from Modelo.DetalleMuestraSismica import DetalleMuestraSismica
from Modelo.MuestraSismica import MuestraSismica
from Modelo.SerieTemporal import SerieTemporal
from Modelo.Sismografo import Sismografo
from Modelo.EstacionSismologica import EstacionSismologica
from Modelo.EventoSismico import EventoSismico
from Modelo.Estado import Estado
from Modelo.CambioEstado import CambioEstado
from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual

# Crear tipos de datos
tipo_velocidad = TipoDeDato("Velocidad de onda", 5.0, "Km/seg")
tipo_frecuencia = TipoDeDato("Frecuencia de onda", 8.0, "Hz")
tipo_longitud = TipoDeDato("Longitud", 0.5, "km/ciclo")

# Crear estaciones sísmicas y sismógrafos
estacion_central = EstacionSismologica("Estación Central")
estacion_norte = EstacionSismologica("Estación Norte")
estacion_sur = EstacionSismologica("Estación Sur")

sismografo_central = Sismografo("SISM001")
sismografo_central.setEstacionSismologica(estacion_central)

sismografo_norte = Sismografo("SISM002")
sismografo_norte.setEstacionSismologica(estacion_norte)

sismografo_sur = Sismografo("SISM003")
sismografo_sur.setEstacionSismologica(estacion_sur)

# Crear series temporales
fecha_inicio = datetime(2025, 2, 21, 19, 5, 41)

# Serie temporal de estación central
serie_central = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioMuestras=fecha_inicio,
    frecuenciaMuestreo="50 Hz"
)
serie_central.setSismografo(sismografo_central)

# Serie temporal de estación norte
serie_norte = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioMuestras=fecha_inicio,
    frecuenciaMuestreo="50 Hz"
)
serie_norte.setSismografo(sismografo_norte)

# Serie temporal de estación sur
serie_sur = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioMuestras=fecha_inicio,
    frecuenciaMuestreo="50 Hz"
)
serie_sur.setSismografo(sismografo_sur)

# Crear muestras sísmicas para cada serie
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

# Agregar muestras a las series temporales
serie_central.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 5.0, 10.0, 0.7),   # Inicio suave
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 6.5, 10.0, 0.69), # Incremento gradual
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 8.0, 10.1, 0.68), # Pico
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 6.0, 10.1, 0.67), # Descenso
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 4.5, 10.2, 0.66)  # Estabilización
]

serie_norte.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 8.0, 10.1, 0.71),  # Inicio alto
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 7.0, 10.1, 0.70), # Descenso rápido
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 9.5, 10.2, 0.69), # Pico máximo
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 8.5, 10.2, 0.68), # Mantiene alto
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 7.5, 10.3, 0.67)  # Descenso gradual
]

serie_sur.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 3.0, 9.9, 0.69),   # Inicio muy bajo
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 4.5, 9.9, 0.68),  # Incremento moderado
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 3.5, 10.0, 0.67), # Oscilación
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 5.0, 10.0, 0.66), # Pico moderado
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 2.5, 10.1, 0.65)  # Caída final
]

# Crear evento sísmico
evento = EventoSismico(
    fechaHoraOcurrencia=datetime(2025, 2, 21, 19, 5, 41),
    valorMagnitud=5.5,
    latitudHipocentro=-34.6037,
    longitudHipocentro=-58.3816,
    latitudEpicentro=-34.6037,
    longitudEpicentro=-58.3816
)

# Agregar series temporales al evento
evento.agregarSerieTemporal(serie_central)
evento.agregarSerieTemporal(serie_norte)
evento.agregarSerieTemporal(serie_sur)

# Crear estado auto-detectado y agregarlo al evento
estado_auto_detectado = Estado("EventoSismico", "AutoDetectado")
cambio_estado = CambioEstado(fechaHoraInicio=datetime.now(), fechaHoraFin=None)
cambio_estado.setEstado(estado_auto_detectado)
evento.agregarCambioEstado(cambio_estado)

# Crear gestor de revisión manual
gestor_revision = GestorRegistrarResultadoDeRevisionManual()

# Simular el flujo de revisión manual
print("\n1. Buscando eventos sísmicos no revisados...")
gestor_revision.buscarEventosSimicosNoRevisados([evento])
print(f"Eventos no revisados encontrados: {len(gestor_revision.listaEventosSimicosNoRevisados)}")

print("\n2. Seleccionando evento sísmico...")
gestor_revision.eventoSismicoSeleccionado = evento

print("\n3. Buscando datos de series temporales...")
gestor_revision.buscarDatosSeriesTemporales()
print(f"Series temporales encontradas: {len(gestor_revision.seriesTemporalesDeEventoSeleccionado)}")

print("\n4. Ordenando series temporales por estación...")
gestor_revision.ordenarSeriesTemporalesPorEstacionSismologica()
print("Series temporales ordenadas por estación sismológica")

print("\n5. Generando sismogramas...")
gestor_revision.llamarCUGenerarSismograma()
print("Sismogramas generados exitosamente") 