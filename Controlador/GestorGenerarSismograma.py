from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class GestorGenerarSismograma:
    def __init__(self):
        self.seriesTemporales = []  # Lista de series temporales a procesar
        self.sismogramasGenerados = []  # Lista de sismogramas generados

    def generarSismogramasPorEstacion(self, seriesTemporales): # Genera y visualiza un sismograma para cada estación sismológica.
       
        self.seriesTemporales = seriesTemporales
        for serie in self.seriesTemporales:
            # Generar sismograma para esta estación
            sismograma = self.generarSismograma(serie)
            self.sismogramasGenerados.append(sismograma)
            # Visualizar el sismograma
            self.visualizarSismograma(sismograma)

    def generarSismograma(self, serie): # Genera un sismograma a partir de una serie temporal.
        
        # Extraer datos de la serie temporal
        estacion = serie['estacionSismologica']
        sismografo = serie['sismografo']
        fecha_inicio = serie['fechaHoraInicio']
        
        # Procesar las muestras para el sismograma
        tiempos = []
        valores = []
        
        for muestra in serie['muestras']:
            tiempo = muestra['fechaHora']
            # Usar el valor de velocidad de onda para el sismograma
            for detalle in muestra['detalles']:
                if detalle['denominacion'] == 'Velocidad de onda':
                    tiempos.append(tiempo)
                    valores.append(detalle['valor'])
                    break
        
        return {
            'estacion': estacion,
            'sismografo': sismografo,
            'fecha_inicio': fecha_inicio,
            'tiempos': tiempos,
            'valores': valores
        }

    def visualizarSismograma(self, sismograma): # Utiliza matplotlib para generar un sismograma
      
        plt.figure(figsize=(12, 6))
        
        # Convertir tiempos a minutos desde el inicio para mejor visualización
        tiempos_minutos = [(t - sismograma['fecha_inicio']).total_seconds() / 60 for t in sismograma['tiempos']]
        
        # Crear el gráfico con más detalles
        plt.plot(tiempos_minutos, sismograma['valores'], 'b-o', linewidth=2, markersize=8)
        
        # Personalizar el gráfico
        plt.title(f'Sismograma - Estación: {sismograma["estacion"]}\nSismógrafo: {sismograma["sismografo"]}', 
                 fontsize=14, pad=20)
        plt.xlabel('Tiempo (minutos desde inicio)', fontsize=12)
        plt.ylabel('Velocidad de onda (Km/seg)', fontsize=12)
        
        # Agregar cuadrícula y personalizar
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Ajustar límites del eje Y para mejor visualización
        y_min = min(sismograma['valores']) - 0.2
        y_max = max(sismograma['valores']) + 0.2
        plt.ylim(y_min, y_max)
        
        # Agregar valores en los puntos
        for x, y in zip(tiempos_minutos, sismograma['valores']):
            plt.text(x, y, f'{y:.1f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show() 