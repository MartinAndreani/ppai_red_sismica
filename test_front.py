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

class GeneradorEventos:
    @staticmethod
    def crear_evento(config):
        """Crea un evento sísmico basado en configuración"""
        evento = EventoSismico(
            fechaHoraOcurrencia=config['fecha'],
            valorMagnitud=config['magnitud'],
            latitudHipocentro=config['lat'],
            longitudHipocentro=config['lon'],
            latitudEpicentro=config['lat'],
            longitudEpicentro=config['lon']
        )
        
        evento.setAlcanceSismo(AlcanceSismo(config['alcance']))
        evento.setClasificacionSismo(ClasificacionSismo(
            config['clasificacion']['tipo'],
            config['clasificacion']['prof_min'],
            config['clasificacion']['prof_max']
        ))
        evento.setOrigenDeGeneracion(OrigenDeGeneracion(config['origen']))

        for estacion_config in config['estaciones']:
            sismografo = Sismografo(estacion_config['codigo'])
            sismografo.setEstacionSismologica(EstacionSismologica(estacion_config['nombre']))
            
            serie = SerieTemporal(
                condicionAlarma=False,
                fechaHoraInicioMuestras=config['fecha'],
                frecuenciaMuestreo=estacion_config['frecuencia']
            )
            serie.setSismografo(sismografo)
            
            muestra = MuestraSismica(config['fecha'])
            for tipo_config in estacion_config['muestras']:
                detalle = DetalleMuestraSismica(tipo_config['valor'])
                detalle.setTipoDeDato(TipoDeDato(
                    tipo_config['nombre'],
                    tipo_config['valor_ref'],
                    tipo_config['unidad']
                ))
                muestra.detalles.append(detalle)
            
            serie.muestras = [muestra]
            evento.agregarSerieTemporal(serie)

        estado = Estado("EventoSismico", config['estado'])
        cambio = CambioEstado(
            fechaHoraInicio=datetime.now(),
            fechaHoraFin=None,
            estado=estado
        )
        evento.agregarCambioEstado(cambio)
        
        return evento

    @staticmethod
    def generar_eventos_test(configuraciones):
        """Genera múltiples eventos a partir de una lista de configuraciones"""
        return [GeneradorEventos.crear_evento(config) for config in configuraciones]


# Configuración de ejemplo - ¡Fácil de modificar!
CONFIG_EVENTOS = [
    {
        'fecha': datetime.now(),
        'magnitud': 5.5,
        'lat': -34.60,
        'lon': -58.38,
        'alcance': "Local",
        'clasificacion': {'tipo': "Superficial", 'prof_min': 0, 'prof_max': 70},
        'origen': "Tectónico",
        'estado': "AutoDetectado",
        'estaciones': [
            {
                'codigo': "SISM01",
                'nombre': "Estación Central",
                'frecuencia': "50 Hz",
                'muestras': [
                    {'nombre': "Velocidad", 'valor_ref': 5.0, 'unidad': "km/s", 'valor': 7.0},
                    {'nombre': "Frecuencia", 'valor_ref': 8.0, 'unidad': "Hz", 'valor': 10.0}
                ]
            }
        ]
    },
    {
        'fecha': datetime.now() - timedelta(days=1),
        'magnitud': 6.0,
        'lat': -35.00,
        'lon': -58.50,
        'alcance': "Regional",
        'clasificacion': {'tipo': "Intermedio", 'prof_min': 70, 'prof_max': 300},
        'origen': "Volcánico",
        'estado': "AutoDetectado",
        'estaciones': [
            {
                'codigo': "SISM02",
                'nombre': "Estación Norte",
                'frecuencia': "100 Hz",
                'muestras': [
                    {'nombre': "Velocidad", 'valor_ref': 5.0, 'unidad': "km/s", 'valor': 7.5},
                    {'nombre': "Frecuencia", 'valor_ref': 8.0, 'unidad': "Hz", 'valor': 12.0}
                ]
            }
        ]
    }
    # Puedes agregar más configuraciones de eventos aquí...
]

# Uso:
eventos = GeneradorEventos.generar_eventos_test(CONFIG_EVENTOS)