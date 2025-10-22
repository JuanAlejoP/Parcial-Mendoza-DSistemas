from src.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie para plantar"""

    def __init__(self, tipo_cultivo: str, superficie_requerida: float, superficie_disponible: float):
        message = (f"Superficie insuficiente para plantar {tipo_cultivo}. "
                  f"Requerida: {superficie_requerida} m², "
                  f"Disponible: {superficie_disponible} m²")
        super().__init__("ERR_SUP", message)
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible