from src.entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    """Implementación concreta de una Lechuga"""

    def __init__(self, agua: int, superficie: float, variedad: str):
        super().__init__(agua, superficie, requiere_invernadero=True)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad