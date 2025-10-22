"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: arbol.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/arbol.py
# ================================================================================

from typing import Final
from abc import abstractmethod
from src.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """Clase base abstracta para árboles"""

    _cant_arboles: int = 0

    def __init__(self, agua: int, altura: float, superficie: float):
        super().__init__(agua, superficie)
        self._id: Final[int] = Arbol._cant_arboles + 1
        self._altura = altura
        Arbol._cant_arboles += 1

    def get_id(self) -> int:
        return self._id

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa")
        self._altura = altura

    @classmethod
    def get_cant_arboles(cls) -> int:
        return cls._cant_arboles

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        super().set_agua(agua)

# ================================================================================
# ARCHIVO 2/8: cultivo.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: hortaliza.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/hortaliza.py
# ================================================================================

from src.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base abstracta para hortalizas"""

    def __init__(self, agua: int, superficie: float, requiere_invernadero: bool):
        super().__init__(agua, superficie)
        self._requiere_invernadero = requiere_invernadero

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        super().set_agua(agua)

# ================================================================================
# ARCHIVO 4/8: lechuga.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/lechuga.py
# ================================================================================

from src.entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    """Implementación concreta de una Lechuga"""

    def __init__(self, agua: int, superficie: float, variedad: str):
        super().__init__(agua, superficie, requiere_invernadero=True)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

# ================================================================================
# ARCHIVO 5/8: olivo.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/olivo.py
# ================================================================================

from src.entidades.cultivos.arbol import Arbol
from src.entidades.cultivos.tipo_aceituna import TipoAceituna

class Olivo(Arbol):
    """Implementación concreta de un Olivo"""

    def __init__(self, agua: int, altura: float, superficie: float, tipo_aceituna: TipoAceituna):
        super().__init__(agua, altura, superficie)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

# ================================================================================
# ARCHIVO 6/8: pino.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/pino.py
# ================================================================================

from src.entidades.cultivos.arbol import Arbol

class Pino(Arbol):
    """Implementación concreta de un Pino"""

    def __init__(self, agua: int, altura: float, superficie: float, variedad: str):
        super().__init__(agua, altura, superficie)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

# ================================================================================
# ARCHIVO 7/8: tipo_aceituna.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """Enumeración de tipos de aceitunas"""
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ================================================================================
# ARCHIVO 8/8: zanahoria.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/zanahoria.py
# ================================================================================

from src.entidades.cultivos.hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """Implementación concreta de una Zanahoria"""

    def __init__(self, agua: int, superficie: float, is_baby_carrot: bool):
        super().__init__(agua, superficie, requiere_invernadero=False)
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby: bool) -> None:
        self._is_baby_carrot = is_baby

