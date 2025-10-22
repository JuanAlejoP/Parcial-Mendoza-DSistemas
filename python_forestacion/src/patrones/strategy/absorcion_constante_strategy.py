from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante para hortalizas"""

    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Retorna una cantidad constante de absorción"""
        return self._cantidad