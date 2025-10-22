from abc import ABC, abstractmethod
from src.entidades.cultivos.cultivo import Cultivo
from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """Clase base abstracta para servicios de cultivos"""

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: Cultivo) -> int:
        """Absorbe agua usando la estrategia configurada"""
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(cultivo)
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra los datos específicos del cultivo"""
        pass