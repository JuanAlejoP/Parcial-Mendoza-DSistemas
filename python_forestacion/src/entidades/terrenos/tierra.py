from typing import Optional, List, Final
from src.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """Clase que representa un terreno para cultivo"""

    def __init__(self, id_padron: int, superficie: float, domicilio: str):
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")

        self._id: Final[int] = id_padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional[Plantacion] = None

    def get_id(self) -> int:
        return self._id

    def get_superficie(self) -> float:
        return self._superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional[Plantacion]:
        return self._finca

    def set_finca(self, finca: Plantacion) -> None:
        self._finca = finca