from typing import Final
from src.entidades.terrenos.tierra import Tierra
from src.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Clase que representa un registro oficial forestal"""

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, 
                 propietario: str, avaluo: float):
        self._id_padron: Final[int] = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo