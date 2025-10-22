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