"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: agua_agotada_exception.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/agua_agotada_exception.py
# ================================================================================

from src.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente agua para regar"""

    def __init__(self, agua_disponible: int, agua_minima: int):
        message = (f"Agua insuficiente para regar. "
                  f"Disponible: {agua_disponible}L, "
                  f"Mínima requerida: {agua_minima}L")
        super().__init__("ERR_AGUA", message)
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def get_agua_minima(self) -> int:
        return self._agua_minima

# ================================================================================
# ARCHIVO 2/5: forestacion_exception.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/forestacion_exception.py
# ================================================================================

class ForestacionException(Exception):
    """Excepción base para el sistema de forestación"""

    def __init__(self, error_code: str, message: str):
        super().__init__(message)
        self._error_code = error_code
        self._user_message = message

    def get_error_code(self) -> str:
        return self._error_code

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"[{self._error_code}] {self._user_message}"

# ================================================================================
# ARCHIVO 3/5: mensajes_exception.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/mensajes_exception.py
# ================================================================================

"""Enums y constantes de mensajes de error."""

from enum import Enum, auto


class TipoOperacion(Enum):
    """Tipo de operación de persistencia."""
    LECTURA = auto()
    ESCRITURA = auto()

# ================================================================================
# ARCHIVO 4/5: persistencia_exception.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: superficie_insuficiente_exception.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/superficie_insuficiente_exception.py
# ================================================================================

from src.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie para plantar"""

    def __init__(self, tipo_cultivo: str, superficie_requerida: float, superficie_disponible: float):
        message = (f"Superficie insuficiente para plantar {tipo_cultivo}. "
                  f"Requerida: {superficie_requerida} m², "
                  f"Disponible: {superficie_disponible} m²")
        super().__init__("ERR_SUP", message)
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

