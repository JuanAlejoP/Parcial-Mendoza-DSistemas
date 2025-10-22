"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: arbol_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/arbol_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/7: cultivo_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/cultivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/7: cultivo_service_registry.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from typing import Dict, Type, Optional, List
from threading import Lock
from src.entidades.cultivos.cultivo import Cultivo
from src.entidades.cultivos.pino import Pino
from src.entidades.cultivos.olivo import Olivo
from src.entidades.cultivos.lechuga import Lechuga
from src.entidades.cultivos.zanahoria import Zanahoria
from src.servicios.cultivos.cultivo_service import CultivoService
from src.servicios.cultivos.pino_service import PinoService
from src.servicios.cultivos.olivo_service import OlivoService
from src.servicios.cultivos.lechuga_service import LechugaService
from src.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """Singleton para el registro de servicios de cultivos"""

    _instance: Optional['CultivoServiceRegistry'] = None
    _lock = Lock()

    def __new__(cls) -> 'CultivoServiceRegistry':
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        self._initialized = getattr(self, '_initialized', False)
        if not self._initialized:
            self._initialize_services()

    def _initialize_services(self) -> None:
        """Inicializa los servicios y handlers"""
        self._initialized = True
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Registry para evitar isinstance()
        self._absorber_agua_handlers = {
            Pino: self._pino_service,
            Olivo: self._olivo_service,
            Lechuga: self._lechuga_service,
            Zanahoria: self._zanahoria_service
        }

        self._mostrar_datos_handlers = self._absorber_agua_handlers.copy()

    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """Obtiene la única instancia del registry"""
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: Cultivo) -> int:
        """Delega la absorción de agua al servicio correspondiente"""
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        return self._absorber_agua_handlers[tipo].absorver_agua(cultivo)

    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Delega la visualización al servicio correspondiente"""
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        self._mostrar_datos_handlers[tipo].mostrar_datos(cultivo)

# ================================================================================
# ARCHIVO 4/7: lechuga_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/lechuga_service.py
# ================================================================================

from src.servicios.cultivos.cultivo_service import CultivoService
from src.entidades.cultivos.lechuga import Lechuga
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class LechugaService(CultivoService):
    """Servicio específico para lechugas"""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))  # 1L constante

    def mostrar_datos(self, lechuga: Lechuga) -> None:
        print(f"Cultivo: Lechuga\n"
              f"Superficie: {lechuga.get_superficie()} m²\n"
              f"Agua almacenada: {lechuga.get_agua()} L\n"
              f"Variedad: {lechuga.get_variedad()}\n"
              f"Invernadero: {lechuga.get_requiere_invernadero()}\n")

# ================================================================================
# ARCHIVO 5/7: olivo_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/olivo_service.py
# ================================================================================

from src.servicios.cultivos.arbol_service import ArbolService
from src.entidades.cultivos.olivo import Olivo
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class OlivoService(ArbolService):
    """Servicio específico para olivos"""

    # Constante para crecimiento
    INCREMENTO_ALTURA = 0.01  # metros por riego

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: Olivo) -> int:
        agua = super().absorver_agua(olivo)
        self.crecer(olivo, self.INCREMENTO_ALTURA)
        return agua

    def mostrar_datos(self, olivo: Olivo) -> None:
        print(f"Cultivo: Olivo\n"
              f"Superficie: {olivo.get_superficie()} m²\n"
              f"Agua almacenada: {olivo.get_agua()} L\n"
              f"ID: {olivo.get_id()}\n"
              f"Altura: {olivo.get_altura()} m\n"
              f"Tipo de aceituna: {olivo.get_tipo_aceituna().name}\n")

# ================================================================================
# ARCHIVO 6/7: pino_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/pino_service.py
# ================================================================================

from src.servicios.cultivos.arbol_service import ArbolService
from src.entidades.cultivos.pino import Pino
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(ArbolService):
    """Servicio específico para pinos"""

    # Constante para crecimiento
    INCREMENTO_ALTURA = 0.10  # metros por riego

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: Pino) -> int:
        agua = super().absorver_agua(pino)
        self.crecer(pino, self.INCREMENTO_ALTURA)
        return agua

    def mostrar_datos(self, pino: Pino) -> None:
        print(f"Cultivo: Pino\n"
              f"Superficie: {pino.get_superficie()} m²\n"
              f"Agua almacenada: {pino.get_agua()} L\n"
              f"ID: {pino.get_id()}\n"
              f"Altura: {pino.get_altura()} m\n"
              f"Variedad: {pino.get_variedad()}\n")

# ================================================================================
# ARCHIVO 7/7: zanahoria_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/zanahoria_service.py
# ================================================================================

from src.servicios.cultivos.cultivo_service import CultivoService
from src.entidades.cultivos.zanahoria import Zanahoria
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    """Servicio específico para zanahorias"""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))  # 2L constante

    def mostrar_datos(self, zanahoria: Zanahoria) -> None:
        tipo = "Baby carrot" if zanahoria.is_baby_carrot() else "Regular"
        print(f"Cultivo: Zanahoria\n"
              f"Superficie: {zanahoria.get_superficie()} m²\n"
              f"Agua almacenada: {zanahoria.get_agua()} L\n"
              f"Tipo: {tipo}\n"
              f"Invernadero: {zanahoria.get_requiere_invernadero()}\n")

