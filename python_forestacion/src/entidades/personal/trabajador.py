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