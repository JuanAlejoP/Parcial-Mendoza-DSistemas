"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: plantacion.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/3: registro_forestal.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/registro_forestal.py
# ================================================================================

from typing import Final
from src.entidades.terrenos.tierra import Tierra
from src.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Clase que representa un registro oficial forestal"""

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, 
                 propietario: str, avaluo: float):
        self._id_padron: Final[int] = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

# ================================================================================
# ARCHIVO 3/3: tierra.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/tierra.py
# ================================================================================

from typing import Optional, List, Final
from src.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """Clase que representa un terreno para cultivo"""

    def __init__(self, id_padron: int, superficie: float, domicilio: str):
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")

        self._id: Final[int] = id_padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional[Plantacion] = None

    def get_id(self) -> int:
        return self._id

    def get_superficie(self) -> float:
        return self._superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional[Plantacion]:
        return self._finca

    def set_finca(self, finca: Plantacion) -> None:
        self._finca = finca

