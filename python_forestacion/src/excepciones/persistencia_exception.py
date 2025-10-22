from enum import Enum
from src.excepciones.forestacion_exception import ForestacionException

class TipoOperacion(Enum):
    """Tipos de operaciones de persistencia"""
    LECTURA = "LECTURA"
    ESCRITURA = "ESCRITURA"

class PersistenciaException(ForestacionException):
    """Excepción lanzada cuando hay problemas de persistencia"""

    def __init__(self, tipo_operacion: TipoOperacion, nombre_archivo: str, mensaje: str):
        super().__init__("ERR_PERS", mensaje)
        self._tipo_operacion = tipo_operacion
        self._nombre_archivo = nombre_archivo

    @staticmethod
    def from_io_exception(tipo_operacion: TipoOperacion, nombre_archivo: str, e: Exception) -> 'PersistenciaException':
        return PersistenciaException(
            tipo_operacion,
            nombre_archivo,
            f"Error de E/S en {tipo_operacion.value}: {str(e)}"
        )

    @staticmethod
    def from_class_not_found_exception(nombre_archivo: str) -> 'PersistenciaException':
        return PersistenciaException(
            TipoOperacion.LECTURA,
            nombre_archivo,
            "Error de deserialización: Clase no encontrada"
        )

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo