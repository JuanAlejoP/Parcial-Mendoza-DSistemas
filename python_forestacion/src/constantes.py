"""
Constantes centralizadas para todo el sistema de gestión forestal.
NUNCA hardcodear valores mágicos - siempre usar estas constantes.
"""

# Cultivos - Superficies (m²)
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

# Agua - Cantidades iniciales (litros)
AGUA_INICIAL_PLANTACION = 500
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

# Altura inicial árboles (metros)
ALTURA_INICIAL_PINO = 1.0
ALTURA_INICIAL_OLIVO = 0.5

# Crecimiento por riego (metros)
CRECIMIENTO_PINO = 0.10
CRECIMIENTO_OLIVO = 0.01

# Riego
AGUA_POR_RIEGO = 10  # litros por operación de riego
TEMP_MIN_RIEGO = 8  # °C
TEMP_MAX_RIEGO = 15  # °C
HUMEDAD_MAX_RIEGO = 50  # %

# Absorción de agua (litros)
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

# Temporada (meses)
MES_INICIO_VERANO = 3  # marzo
MES_FIN_VERANO = 8  # agosto

# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
INTERVALO_CONTROL_RIEGO = 2.5  # segundos

SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50  # °C
SENSOR_HUMEDAD_MIN = 0  # %
SENSOR_HUMEDAD_MAX = 100  # %

# Threads
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"