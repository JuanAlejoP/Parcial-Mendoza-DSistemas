from datetime import date
from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción estacional para árboles"""

    # Constantes para absorción estacional
    ABSORCION_SEASONAL_VERANO = 5  # L
    ABSORCION_SEASONAL_INVIERNO = 2  # L
    MES_INICIO_VERANO = 3  # marzo
    MES_FIN_VERANO = 8  # agosto

    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Calcula absorción según la estación"""
        mes_actual = date.today().month
        if self.MES_INICIO_VERANO <= mes_actual <= self.MES_FIN_VERANO:
            return self.ABSORCION_SEASONAL_VERANO
        return self.ABSORCION_SEASONAL_INVIERNO