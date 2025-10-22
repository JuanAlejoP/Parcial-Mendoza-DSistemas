"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: absorcion_agua_strategy.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Estrategia abstracta para el cálculo de absorción de agua"""

    @abstractmethod
    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Calcula la cantidad de agua que absorberá el cultivo"""
        pass

# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_constante_strategy.py
# ================================================================================

from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante para hortalizas"""

    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Retorna una cantidad constante de absorción"""
        return self._cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_seasonal_strategy.py
# ================================================================================

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

