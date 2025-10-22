from src.entidades.cultivos.hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """Implementación concreta de una Zanahoria"""

    def __init__(self, agua: int, superficie: float, is_baby_carrot: bool):
        super().__init__(agua, superficie, requiere_invernadero=False)
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby: bool) -> None:
        self._is_baby_carrot = is_baby