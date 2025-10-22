"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: apto_medico.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/apto_medico.py
# ================================================================================

from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class AptoMedico:
    """Clase que representa el apto médico de un trabajador"""

    _apto: bool
    _fecha_emision: date
    _observaciones: str = ""

    def esta_apto(self) -> bool:
        return self._apto

    def set_apto(self, apto: bool) -> None:
        self._apto = apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def get_resumen(self) -> str:
        estado = "APTO" if self._apto else "NO APTO"
        return f"Estado: {estado}, Fecha: {self._fecha_emision}, Obs: {self._observaciones}"

# ================================================================================
# ARCHIVO 2/4: herramienta.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/herramienta.py
# ================================================================================

from typing import Final

class Herramienta:
    """Clase que representa una herramienta de trabajo"""

    def __init__(self, id_herramienta: int, nombre: str, operativa: bool = True):
        self._id: Final[int] = id_herramienta
        self._nombre = nombre
        self._operativa = operativa

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def is_operativa(self) -> bool:
        return self._operativa

    def set_operativa(self, operativa: bool) -> None:
        self._operativa = operativa

# ================================================================================
# ARCHIVO 3/4: tarea.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/tarea.py
# ================================================================================

from dataclasses import dataclass
from datetime import date
from typing import Final

@dataclass
class Tarea:
    """Clase que representa una tarea asignada a un trabajador"""

    _id: Final[int]
    _fecha: date
    _descripcion: str
    _estado: bool = False

    def get_id(self) -> int:
        return self._id

    def get_fecha(self) -> date:
        return self._fecha

    def get_descripcion(self) -> str:
        return self._descripcion

    def is_estado(self) -> bool:
        return self._estado

    def set_estado(self, estado: bool) -> None:
        self._estado = estado

    def set_completada(self, completada: bool) -> None:
        """Marca la tarea como completada o no completada"""
        self.set_estado(completada)

# ================================================================================
# ARCHIVO 4/4: trabajador.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/trabajador.py
# ================================================================================

from typing import List, Optional, Final
from datetime import date
from src.entidades.personal.apto_medico import AptoMedico
from src.entidades.personal.tarea import Tarea

class Trabajador:
    """Clase que representa un trabajador"""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni: Final[int] = dni
        self._nombre = nombre
        self._tareas = tareas.copy()
        self._apto_medico: Optional[AptoMedico] = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        self._apto_medico = apto_medico

    def get_tareas(self) -> List[Tarea]:
        return self._tareas.copy()

    def asignar_apto_medico(self, apto: bool, fecha: date, obs: str = "") -> None:
        self._apto_medico = AptoMedico(apto, fecha, obs)

