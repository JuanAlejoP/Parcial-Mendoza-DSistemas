from abc import ABC, abstractmethod
from typing import Protocol

class Cultivo(ABC):
    """Interfaz base para todos los cultivos"""
    
    EDAD_MAXIMA = 20

    def __init__(self, agua: int, superficie: float):
        self._agua = agua
        self._superficie = superficie
    
    def get_superficie(self) -> float:
        """Retorna la superficie ocupada por el cultivo en metros cuadrados"""
        return self._superficie
    
    def get_agua(self) -> int:
        """Retorna la cantidad de agua almacenada por el cultivo en litros"""
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """Establece la cantidad de agua almacenada por el cultivo"""
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua = agua