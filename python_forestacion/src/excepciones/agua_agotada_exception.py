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