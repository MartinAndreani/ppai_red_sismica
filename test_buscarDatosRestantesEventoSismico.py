from datetime import datetime
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
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 7.0, 10.0, 0.7),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 7.02, 10.0, 0.69)
]

serie_norte.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 7.1, 10.1, 0.71),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 7.12, 10.1, 0.70)
]

serie_sur.muestras = [
    crear_muestra(datetime(2025, 2, 21, 19, 5, 41), 6.9, 9.9, 0.69),
    crear_muestra(datetime(2025, 2, 21, 19, 10, 41), 6.92, 9.9, 0.68)
]

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

# Agregar series temporales en orden no alfabético
evento.agregarSerieTemporal(serie_norte)
evento.agregarSerieTemporal(serie_sur)
evento.agregarSerieTemporal(serie_central)

# Crear gestor y ejecutar
gestor = GestorRegistrarResultadoDeRevisionManual()
gestor.eventoSismicoSeleccionado = evento
gestor.buscarDatosRestantesEventoSismico()
gestor.buscarDatosSeriesTemporales()

print("\nDatos restantes del evento sísmico:")
for datos in gestor.listaDatosRestantesDeEventoSeleccionado:
    print(f"\nAlcance: {datos['alcance']}")
    print(f"Clasificación: {datos['clasificacion']['nombre']}")
    print(f"  Profundidad desde: {datos['clasificacion']['profundidadDesde']} km")
    print(f"  Profundidad hasta: {datos['clasificacion']['profundidadHasta']} km")
    print(f"Origen: {datos['origen']}")

print("\nSeries Temporales (sin ordenar):")
for serie in gestor.seriesTemporalesDeEventoSeleccionado:
    print(f"\nSerie Temporal - Estación Sismológica: {serie['estacionSismologica']}")
    print(f"Sismógrafo: {serie['sismografo']}")
    print(f"Fecha inicio: {serie['fechaHoraInicio']}")
    print("\nMuestras:")
    for muestra in serie['muestras']:
        print(f"\n  Fecha/Hora: {muestra['fechaHora']}")
        print("  Detalles:")
        for detalle in muestra['detalles']:
            print(f"    {detalle['denominacion']}: {detalle['valor']} {detalle['unidadMedida']} (Umbral: {detalle['valorUmbral']})")

# Ordenar las series temporales
gestor.ordenarSeriesTemporalesPorEstacionSismologica()

print("\nSeries Temporales (ordenadas por estación):")
for serie in gestor.seriesTemporalesDeEventoSeleccionado:
    print(f"\nSerie Temporal - Estación Sismológica: {serie['estacionSismologica']}")
    print(f"Sismógrafo: {serie['sismografo']}")
    print(f"Fecha inicio: {serie['fechaHoraInicio']}")
    print("\nMuestras:")
    for muestra in serie['muestras']:
        print(f"\n  Fecha/Hora: {muestra['fechaHora']}")
        print("  Detalles:")
        for detalle in muestra['detalles']:
            print(f"    {detalle['denominacion']}: {detalle['valor']} {detalle['unidadMedida']} (Umbral: {detalle['valorUmbral']})") 