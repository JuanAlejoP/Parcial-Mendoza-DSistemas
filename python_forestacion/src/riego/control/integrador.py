"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/control
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: control_riego_task.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/control/control_riego_task.py
# ================================================================================

import threading
import time
from src.patrones.observer.observable import Observer
from src.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from src.riego.sensores.humedad_reader_task import HumedadReaderTask
from src.entidades.terrenos.plantacion import Plantacion
from src.servicios.terrenos.plantacion_service import PlantacionService
from src.excepciones.agua_agotada_exception import AguaAgotadaException

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador de riego automático basado en sensores"""

    # Constantes de control
    INTERVALO_CONTROL = 2.5  # segundos
    TEMP_MIN_RIEGO = 8.0  # °C
    TEMP_MAX_RIEGO = 15.0  # °C
    HUMEDAD_MAX_RIEGO = 50.0  # %

    def __init__(self, sensor_temperatura: TemperaturaReaderTask,
                 sensor_humedad: HumedadReaderTask,
                 plantacion: Plantacion,
                 plantacion_service: PlantacionService):
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        self._ultima_temperatura = sensor_temperatura.get_ultima_temperatura()
        self._ultima_humedad = sensor_humedad.get_ultima_humedad()

        # Suscribirse a los sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def detener(self) -> None:
        """Detiene la tarea de control"""
        self._detenido.set()
        self._sensor_temperatura.eliminar_observador(self)
        self._sensor_humedad.eliminar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Recibe actualizaciones de los sensores"""
        if isinstance(self._sensor_temperatura, TemperaturaReaderTask):
            self._ultima_temperatura = evento
        else:
            self._ultima_humedad = evento

    def run(self) -> None:
        """Ejecuta el control de riego"""
        while not self._detenido.is_set():
            try:
                # Verificar condiciones de riego
                if (self.TEMP_MIN_RIEGO <= self._ultima_temperatura <= self.TEMP_MAX_RIEGO and
                    self._ultima_humedad < self.HUMEDAD_MAX_RIEGO):
                    # Condiciones óptimas - regar
                    self._plantacion_service.regar(self._plantacion)
            except AguaAgotadaException:
                print("Control de riego detenido: agua agotada")
                self.detener()
            finally:
                time.sleep(self.INTERVALO_CONTROL)

