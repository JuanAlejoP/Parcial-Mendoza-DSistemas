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