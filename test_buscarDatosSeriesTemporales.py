from datetime import datetime
from Modelo.TipoDeDato import TipoDeDato
from Modelo.DetalleMuestraSismica import DetalleMuestraSismica
from Modelo.MuestraSismica import MuestraSismica
from Modelo.SerieTemporal import SerieTemporal
from Modelo.Sismografo import Sismografo
from Modelo.EstacionSismologica import EstacionSismologica
from Modelo.EventoSismico import EventoSismico
from Controlador.GestorRegistrarResultadoDeRevisionManual import GestorRegistrarResultadoDeRevisionManual

# Crear tipos de datos
tipo_velocidad = TipoDeDato("Velocidad de onda", 5.0, "Km/seg")
tipo_frecuencia = TipoDeDato("Frecuencia de onda", 8.0, "Hz")
tipo_longitud = TipoDeDato("Longitud", 0.5, "km/ciclo")

# Crear estación sísmica y sismógrafo
estacion = EstacionSismologica("Estación Central")
sismografo = Sismografo("SISM001")
sismografo.setEstacionSismologica(estacion)

# Crear serie temporal
fecha_inicio = datetime(2025, 2, 21, 19, 5, 41)
serie = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioMuestras=fecha_inicio,
    frecuenciaMuestreo="50 Hz"
)
serie.setSismografo(sismografo)

# Crear muestras sísmicas
muestra1 = MuestraSismica(datetime(2025, 2, 21, 19, 5, 41))
detalle1_1 = DetalleMuestraSismica(7.0)
detalle1_1.setTipoDeDato(tipo_velocidad)
detalle1_2 = DetalleMuestraSismica(10.0)
detalle1_2.setTipoDeDato(tipo_frecuencia)
detalle1_3 = DetalleMuestraSismica(0.7)
detalle1_3.setTipoDeDato(tipo_longitud)
muestra1.detalles = [detalle1_1, detalle1_2, detalle1_3]

muestra2 = MuestraSismica(datetime(2025, 2, 21, 19, 10, 41))
detalle2_1 = DetalleMuestraSismica(7.02)
detalle2_1.setTipoDeDato(tipo_velocidad)
detalle2_2 = DetalleMuestraSismica(10.0)
detalle2_2.setTipoDeDato(tipo_frecuencia)
detalle2_3 = DetalleMuestraSismica(0.69)
detalle2_3.setTipoDeDato(tipo_longitud)
muestra2.detalles = [detalle2_1, detalle2_2, detalle2_3]

# Agregar muestras a la serie temporal
serie.muestras = [muestra1, muestra2]

# Crear evento sísmico
evento = EventoSismico(
    fechaHoraOcurrencia=datetime(2025, 2, 21, 19, 5, 41),
    valorMagnitud=5.5,
    latitudHipocentro=-34.6037,
    longitudHipocentro=-58.3816,
    latitudEpicentro=-34.6037,
    longitudEpicentro=-58.3816
)
evento.agregarSerieTemporal(serie)

# Crear gestor y ejecutar
gestor = GestorRegistrarResultadoDeRevisionManual()
gestor.eventoSismicoSeleccionado = evento
gestor.buscarDatosSeriesTemporales()

# Mostrar resultados
print("\nDatos de series temporales encontrados:")
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