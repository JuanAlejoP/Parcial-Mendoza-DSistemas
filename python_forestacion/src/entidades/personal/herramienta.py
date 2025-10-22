from typing import Final

class Herramienta:
    """Clase que representa una herramienta de trabajo"""

    def __init__(self, id_herramienta: int, nombre: str, operativa: bool = True):
        self._id: Final[int] = id_herramienta
        self._nombre = nombre
        self._operativa = operativa

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def is_operativa(self) -> bool:
        return self._operativa

    def set_operativa(self, operativa: bool) -> None:
        self._operativa = operativa