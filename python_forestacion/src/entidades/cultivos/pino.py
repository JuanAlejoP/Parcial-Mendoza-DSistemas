from src.entidades.cultivos.arbol import Arbol

class Pino(Arbol):
    """Implementación concreta de un Pino"""

    def __init__(self, agua: int, altura: float, superficie: float, variedad: str):
        super().__init__(agua, altura, superficie)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad