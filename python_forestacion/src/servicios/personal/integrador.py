"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/personal
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: trabajador_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/personal/trabajador_service.py
# ================================================================================

"""Servicio para gestión de trabajadores."""

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.entidades.personal.trabajador import Trabajador
    from src.entidades.personal.apto_medico import AptoMedico
    from src.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """Servicio de gestión de trabajadores."""

    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ) -> None:
        """
        Asigna apto médico a un trabajador.
        
        Args:
            trabajador: Trabajador a asignar apto
            apto: Si está apto o no
            fecha_emision: Fecha de emisión del apto
            observaciones: Observaciones médicas opcionales
        """
        from src.entidades.personal.apto_medico import AptoMedico
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        print(f"Apto médico asignado a {trabajador.get_nombre()}")

    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Hace que el trabajador ejecute sus tareas.
        
        Args:
            trabajador: Trabajador que ejecutará tareas
            fecha: Fecha en que se realizan las tareas
            util: Herramienta a utilizar
            
        Returns:
            True si pudo trabajar, False si no tiene apto médico
        """
        if not trabajador.get_apto_medico() or not trabajador.get_apto_medico().esta_apto():
            print(f"{trabajador.get_nombre()} no puede trabajar - sin apto médico")
            return False

        # Obtener tareas ordenadas por ID descendente
        tareas = sorted(
            trabajador.get_tareas(),
            key=lambda t: t.get_id(),
            reverse=True
        )

        # Ejecutar cada tarea
        for tarea in tareas:
            print(f"El trabajador {trabajador.get_nombre()} realizó la tarea "
                  f"{tarea.get_id()} {tarea.get_descripcion()} con herramienta: "
                  f"{util.get_nombre()}")
            tarea.set_completada(True)

        return True

