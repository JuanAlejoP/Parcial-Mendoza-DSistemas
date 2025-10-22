from abc import ABC, abstractmethod
from datetime import date
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Estrategia abstracta para el cálculo de absorción de agua"""

    @abstractmethod
    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Calcula la cantidad de agua que absorberá el cultivo"""
        pass