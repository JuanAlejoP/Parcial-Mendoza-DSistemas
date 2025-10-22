from src.entidades.cultivos.arbol import Arbol
from src.entidades.cultivos.tipo_aceituna import TipoAceituna

class Olivo(Arbol):
    """Implementación concreta de un Olivo"""

    def __init__(self, agua: int, altura: float, superficie: float, tipo_aceituna: TipoAceituna):
        super().__init__(agua, altura, superficie)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna