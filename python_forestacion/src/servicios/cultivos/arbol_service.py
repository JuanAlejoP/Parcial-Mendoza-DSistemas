from src.servicios.cultivos.cultivo_service import CultivoService
from src.entidades.cultivos.arbol import Arbol
from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """Servicio base para árboles"""

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol: Arbol, incremento: float) -> None:
        if incremento < 0:
            raise ValueError("El incremento debe ser positivo")
        arbol.set_altura(arbol.get_altura() + incremento)