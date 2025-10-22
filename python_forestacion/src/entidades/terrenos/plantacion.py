from typing import List, Optional, Final
from copy import deepcopy
from src.entidades.cultivos.cultivo import Cultivo
from src.entidades.personal.trabajador import Trabajador

class Plantacion:
    """Clase que representa una plantación o finca"""

    def __init__(self, nombre: str, superficie: float, agua: int = 500):
        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List[Cultivo] = []
        self._trabajadores: List[Trabajador] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa")
        self._agua_disponible = agua

    def get_cultivos(self) -> List[Cultivo]:
        return deepcopy(self._cultivos)

    def get_cultivos_interno(self) -> List[Cultivo]:
        return self._cultivos

    def get_trabajadores(self) -> List[Trabajador]:
        return deepcopy(self._trabajadores)

    def get_trabajadores_interno(self) -> List[Trabajador]:
        return self._trabajadores

    def set_trabajadores(self, trabajadores: List[Trabajador]) -> None:
        self._trabajadores = deepcopy(trabajadores)
        
    def get_superficie_disponible(self) -> float:
        """Retorna la superficie disponible en la plantación"""
        superficie_ocupada = sum(cultivo.get_superficie() for cultivo in self._cultivos)
        return self._superficie - superficie_ocupada

    def add_cultivo(self, cultivo: Cultivo) -> None:
        """Agrega un cultivo a la plantación"""
        self._cultivos.append(cultivo)

    def remove_cultivo(self, cultivo: Cultivo) -> None:
        """Remueve un cultivo de la plantación, buscando por tipo y atributos"""
        for i, c in enumerate(self._cultivos):
            if (type(c) == type(cultivo) and 
                c.get_superficie() == cultivo.get_superficie() and
                c.get_agua() == cultivo.get_agua()):
                del self._cultivos[i]
                return
        raise ValueError(f"Cultivo {type(cultivo)} no encontrado")