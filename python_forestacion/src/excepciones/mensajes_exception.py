"""Enums y constantes de mensajes de error."""

from enum import Enum, auto


class TipoOperacion(Enum):
    """Tipo de operación de persistencia."""
    LECTURA = auto()
    ESCRITURA = auto()