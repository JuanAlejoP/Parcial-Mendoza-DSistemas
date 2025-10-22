from typing import Final
from abc import abstractmethod
from src.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """Clase base abstracta para árboles"""

    _cant_arboles: int = 0

    def __init__(self, agua: int, altura: float, superficie: float):
        super().__init__(agua, superficie)
        self._id: Final[int] = Arbol._cant_arboles + 1
        self._altura = altura
        Arbol._cant_arboles += 1

    def get_id(self) -> int:
        return self._id

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa")
        self._altura = altura

    @classmethod
    def get_cant_arboles(cls) -> int:
        return cls._cant_arboles

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        super().set_agua(agua)