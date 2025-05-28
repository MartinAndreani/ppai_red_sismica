from datetime import datetime
from Modelo.TipoDeDato import TipoDeDato
from Modelo.DetalleMuestraSismica import DetalleMuestraSismica
from Modelo.MuestraSismica import MuestraSismica
from Modelo.SerieTemporal import SerieTemporal
from Modelo.Sismografo import Sismografo
from Modelo.EstacionSismologica import EstacionSismologica
from Modelo.EventoSismico import EventoSismico
from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual
from Controlador.GestorGenerarSismograma import GestorGenerarSismograma

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
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 7.0, 10.0, 0.7),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 7.02, 10.0, 0.69),
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 7.05, 10.1, 0.68),
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 7.08, 10.1, 0.67),
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 7.10, 10.2, 0.66)
]

serie_norte.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 7.1, 10.1, 0.71),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 7.12, 10.1, 0.70),
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 7.15, 10.2, 0.69),
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 7.18, 10.2, 0.68),
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 7.20, 10.3, 0.67)
]

serie_sur.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 6.9, 9.9, 0.69),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 6.92, 9.9, 0.68),
    crear_muestra(datetime(2025, 2, 21, 19, 15, 41), 6.95, 10.0, 0.67),
    crear_muestra(datetime(2025, 2, 21, 19, 20, 41), 6.98, 10.0, 0.66),
    crear_muestra(datetime(2025, 2, 21, 19, 25, 41), 7.00, 10.1, 0.65)
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

# Crear gestor de revisión manual y obtener series temporales
gestor_revision = GestorRegistrarResultadoDeRevisionManual()
gestor_revision.eventoSismicoSeleccionado = evento
gestor_revision.buscarDatosSeriesTemporales()

# Crear gestor de sismogramas y generar visualizaciones
gestor_sismograma = GestorGenerarSismograma()
gestor_sismograma.generarSismogramasPorEstacion(gestor_revision.seriesTemporalesDeEventoSeleccionado) 