from dataclasses import dataclass
from datetime import date
from typing import Final

@dataclass
class Tarea:
    """Clase que representa una tarea asignada a un trabajador"""

    _id: Final[int]
    _fecha: date
    _descripcion: str
    _estado: bool = False

    def get_id(self) -> int:
        return self._id

    def get_fecha(self) -> date:
        return self._fecha

    def get_descripcion(self) -> str:
        return self._descripcion

    def is_estado(self) -> bool:
        return self._estado

    def set_estado(self, estado: bool) -> None:
        self._estado = estado

    def set_completada(self, completada: bool) -> None:
        """Marca la tarea como completada o no completada"""
        self.set_estado(completada)