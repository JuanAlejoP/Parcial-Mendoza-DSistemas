"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/sensores
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: humedad_reader_task.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/sensores/humedad_reader_task.py
# ================================================================================

import threading
import random
import time
from src.patrones.observer.observable import Observable

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Tarea que lee humedad en segundo plano y notifica a observadores"""

    # Constantes del sensor
    INTERVALO_SENSOR = 3.0  # segundos
    HUMEDAD_MIN = 0.0  # %
    HUMEDAD_MAX = 100.0  # %

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_humedad = 50.0  # humedad inicial por defecto

    def detener(self) -> None:
        """Detiene la tarea de lectura"""
        self._detenido.set()

    def run(self) -> None:
        """Ejecuta la tarea de lectura continua"""
        while not self._detenido.is_set():
            self._ultima_humedad = self._leer_humedad()
            self.notificar_observadores(self._ultima_humedad)
            time.sleep(self.INTERVALO_SENSOR)

    def _leer_humedad(self) -> float:
        """Simula la lectura del sensor de humedad"""
        return random.uniform(self.HUMEDAD_MIN, self.HUMEDAD_MAX)

    def get_ultima_humedad(self) -> float:
        """Retorna la última humedad leída"""
        return self._ultima_humedad

# ================================================================================
# ARCHIVO 2/2: temperatura_reader_task.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/sensores/temperatura_reader_task.py
# ================================================================================

import threading
import random
import time
from src.patrones.observer.observable import Observable

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Tarea que lee temperatura en segundo plano y notifica a observadores"""

    # Constantes del sensor
    INTERVALO_SENSOR = 2.0  # segundos
    TEMP_MIN = -25.0  # °C
    TEMP_MAX = 50.0  # °C

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_temperatura = 20.0  # temperatura inicial por defecto

    def detener(self) -> None:
        """Detiene la tarea de lectura"""
        self._detenido.set()

    def run(self) -> None:
        """Ejecuta la tarea de lectura continua"""
        while not self._detenido.is_set():
            self._ultima_temperatura = self._leer_temperatura()
            self.notificar_observadores(self._ultima_temperatura)
            time.sleep(self.INTERVALO_SENSOR)

    def _leer_temperatura(self) -> float:
        """Simula la lectura del sensor de temperatura"""
        return random.uniform(self.TEMP_MIN, self.TEMP_MAX)

    def get_ultima_temperatura(self) -> float:
        """Retorna la última temperatura leída"""
        return self._ultima_temperatura

