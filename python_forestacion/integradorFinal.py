"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion
Fecha de generacion: 2025-10-22 01:14:01
Total de archivos integrados: 43
Total de directorios procesados: 15
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. main.py
#
# DIRECTORIO: src
#   2. constantes.py
#
# DIRECTORIO: src/entidades/cultivos
#   3. arbol.py
#   4. cultivo.py
#   5. hortaliza.py
#   6. lechuga.py
#   7. olivo.py
#   8. pino.py
#   9. tipo_aceituna.py
#   10. zanahoria.py
#
# DIRECTORIO: src/entidades/personal
#   11. apto_medico.py
#   12. herramienta.py
#   13. tarea.py
#   14. trabajador.py
#
# DIRECTORIO: src/entidades/terrenos
#   15. plantacion.py
#   16. registro_forestal.py
#   17. tierra.py
#
# DIRECTORIO: src/excepciones
#   18. agua_agotada_exception.py
#   19. forestacion_exception.py
#   20. mensajes_exception.py
#   21. persistencia_exception.py
#   22. superficie_insuficiente_exception.py
#
# DIRECTORIO: src/patrones/factory
#   23. cultivo_factory.py
#
# DIRECTORIO: src/patrones/observer
#   24. observable.py
#
# DIRECTORIO: src/patrones/strategy
#   25. absorcion_agua_strategy.py
#   26. absorcion_constante_strategy.py
#   27. absorcion_seasonal_strategy.py
#
# DIRECTORIO: src/riego/control
#   28. control_riego_task.py
#
# DIRECTORIO: src/riego/sensores
#   29. humedad_reader_task.py
#   30. temperatura_reader_task.py
#
# DIRECTORIO: src/servicios/cultivos
#   31. arbol_service.py
#   32. cultivo_service.py
#   33. cultivo_service_registry.py
#   34. lechuga_service.py
#   35. olivo_service.py
#   36. pino_service.py
#   37. zanahoria_service.py
#
# DIRECTORIO: src/servicios/negocio
#   38. fincas_service.py
#   39. paquete.py
#
# DIRECTORIO: src/servicios/personal
#   40. trabajador_service.py
#
# DIRECTORIO: src/servicios/terrenos
#   41. plantacion_service.py
#   42. registro_forestal_service.py
#   43. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/43: main.py
# Directorio: .
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/main.py
# ==============================================================================

"""
Sistema de Gestión Forestal - Demostración de Patrones de Diseño.

Este módulo demuestra el uso de los patrones:
- SINGLETON: CultivoServiceRegistry
- FACTORY METHOD: CultivoFactory para crear cultivos
- OBSERVER: Sensores y control de riego
- STRATEGY: Absorción de agua por tipo de cultivo
"""

import time
from datetime import date

from src.entidades.personal.herramienta import Herramienta
from src.entidades.personal.tarea import Tarea
from src.entidades.personal.trabajador import Trabajador
from src.entidades.terrenos.registro_forestal import RegistroForestal
from src.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from src.servicios.negocio.fincas_service import FincasService
from src.servicios.personal.trabajador_service import TrabajadorService
from src.servicios.terrenos.plantacion_service import PlantacionService
from src.servicios.terrenos.registro_forestal_service import RegistroForestalService
from src.servicios.terrenos.tierra_service import TierraService
from src.riego.control.control_riego_task import ControlRiegoTask
from src.riego.sensores.humedad_reader_task import HumedadReaderTask
from src.riego.sensores.temperatura_reader_task import TemperaturaReaderTask

# Constantes de demostración
SEGUNDOS_DEMO_RIEGO = 20
THREAD_JOIN_TIMEOUT = 2.0


def main():
    """Demostración completa del sistema."""
    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISEÑO")
    print("=" * 70)

    print("\n" + "-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)

    # 1. Demostrar Singleton
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()
    print("[OK] Todos los servicios comparten la misma instancia del Registry")

    # 2. Crear tierra con plantación
    print("\n1. Creando tierra con plantación...")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()

    # 3. Demostrar Factory Method
    print("\n2. Demostrando Factory Method - Creando cultivos...")
    plantacion_service = PlantacionService()
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)

    # 4. Crear trabajador con tareas y apto médico
    print("\n3. Creando trabajador con tareas y apto médico...")
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]
    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    plantacion.set_trabajadores([trabajador])

    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )

    # 5. Ejecutar tareas del trabajador
    print("\n4. Ejecutando tareas del trabajador...")
    herramienta = Herramienta(1, "Pala", True)
    trabajador_service.trabajar(trabajador, date.today(), herramienta)

    # 6. Demostrar Observer y Strategy - Sistema de riego
    print("\n5. Iniciando sistema de riego automático...")
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )

    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    # Dejar sistema funcionando 20 segundos
    print(f"Sistema funcionando por {SEGUNDOS_DEMO_RIEGO} segundos...")
    time.sleep(SEGUNDOS_DEMO_RIEGO)

    # Detener sistema de riego
    print("\n6. Deteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

    # 7. Crear y persistir registro forestal
    print("\n7. Creando y persistiendo registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )

    registro_service = RegistroForestalService()
    registro_service.persistir(registro)

    # 8. Recuperar registro y mostrar datos
    print("\n8. Recuperando y mostrando registro...")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    registro_service.mostrar_datos(registro_leido)

    # 9. Gestionar múltiples fincas
    print("\n9. Demostrando gestión de múltiples fincas...")
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    fincas_service.fumigar(1, "insecto orgánico")

    # 10. Cosechar y empaquetar por tipo
    print("\n10. Cosechando y empaquetando cultivos por tipo...")
    from src.entidades.cultivos.lechuga import Lechuga
    from src.entidades.cultivos.pino import Pino

    # Cosechar lechugas
    caja_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)

    # Cosechar pinos
    caja_pinos = fincas_service.cosechar_y_empaquetar(Pino)

    # Resumen final
    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia única)")
    print("  [OK] FACTORY     - Creación de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorción de agua")
    print("=" * 70)


if __name__ == "__main__":
    main()


################################################################################
# DIRECTORIO: src
################################################################################

# ==============================================================================
# ARCHIVO 2/43: constantes.py
# Directorio: src
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/constantes.py
# ==============================================================================

"""
Constantes centralizadas para todo el sistema de gestión forestal.
NUNCA hardcodear valores mágicos - siempre usar estas constantes.
"""

# Cultivos - Superficies (m²)
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

# Agua - Cantidades iniciales (litros)
AGUA_INICIAL_PLANTACION = 500
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

# Altura inicial árboles (metros)
ALTURA_INICIAL_PINO = 1.0
ALTURA_INICIAL_OLIVO = 0.5

# Crecimiento por riego (metros)
CRECIMIENTO_PINO = 0.10
CRECIMIENTO_OLIVO = 0.01

# Riego
AGUA_POR_RIEGO = 10  # litros por operación de riego
TEMP_MIN_RIEGO = 8  # °C
TEMP_MAX_RIEGO = 15  # °C
HUMEDAD_MAX_RIEGO = 50  # %

# Absorción de agua (litros)
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

# Temporada (meses)
MES_INICIO_VERANO = 3  # marzo
MES_FIN_VERANO = 8  # agosto

# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
INTERVALO_CONTROL_RIEGO = 2.5  # segundos

SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50  # °C
SENSOR_HUMEDAD_MIN = 0  # %
SENSOR_HUMEDAD_MAX = 100  # %

# Threads
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"


################################################################################
# DIRECTORIO: src/entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 3/43: arbol.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 4/43: cultivo.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/43: hortaliza.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/43: lechuga.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/lechuga.py
# ==============================================================================

from src.entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    """Implementación concreta de una Lechuga"""

    def __init__(self, agua: int, superficie: float, variedad: str):
        super().__init__(agua, superficie, requiere_invernadero=True)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

# ==============================================================================
# ARCHIVO 7/43: olivo.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/olivo.py
# ==============================================================================

from src.entidades.cultivos.arbol import Arbol
from src.entidades.cultivos.tipo_aceituna import TipoAceituna

class Olivo(Arbol):
    """Implementación concreta de un Olivo"""

    def __init__(self, agua: int, altura: float, superficie: float, tipo_aceituna: TipoAceituna):
        super().__init__(agua, altura, superficie)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

# ==============================================================================
# ARCHIVO 8/43: pino.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/pino.py
# ==============================================================================

from src.entidades.cultivos.arbol import Arbol

class Pino(Arbol):
    """Implementación concreta de un Pino"""

    def __init__(self, agua: int, altura: float, superficie: float, variedad: str):
        super().__init__(agua, altura, superficie)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

# ==============================================================================
# ARCHIVO 9/43: tipo_aceituna.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """Enumeración de tipos de aceitunas"""
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ==============================================================================
# ARCHIVO 10/43: zanahoria.py
# Directorio: src/entidades/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/cultivos/zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: src/entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 11/43: apto_medico.py
# Directorio: src/entidades/personal
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/apto_medico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 12/43: herramienta.py
# Directorio: src/entidades/personal
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 13/43: tarea.py
# Directorio: src/entidades/personal
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/tarea.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/43: trabajador.py
# Directorio: src/entidades/personal
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/personal/trabajador.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: src/entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 15/43: plantacion.py
# Directorio: src/entidades/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/plantacion.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 16/43: registro_forestal.py
# Directorio: src/entidades/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/registro_forestal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 17/43: tierra.py
# Directorio: src/entidades/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/entidades/terrenos/tierra.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: src/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 18/43: agua_agotada_exception.py
# Directorio: src/excepciones
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/agua_agotada_exception.py
# ==============================================================================

from src.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente agua para regar"""

    def __init__(self, agua_disponible: int, agua_minima: int):
        message = (f"Agua insuficiente para regar. "
                  f"Disponible: {agua_disponible}L, "
                  f"Mínima requerida: {agua_minima}L")
        super().__init__("ERR_AGUA", message)
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def get_agua_minima(self) -> int:
        return self._agua_minima

# ==============================================================================
# ARCHIVO 19/43: forestacion_exception.py
# Directorio: src/excepciones
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """Excepción base para el sistema de forestación"""

    def __init__(self, error_code: str, message: str):
        super().__init__(message)
        self._error_code = error_code
        self._user_message = message

    def get_error_code(self) -> str:
        return self._error_code

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"[{self._error_code}] {self._user_message}"

# ==============================================================================
# ARCHIVO 20/43: mensajes_exception.py
# Directorio: src/excepciones
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/mensajes_exception.py
# ==============================================================================

"""Enums y constantes de mensajes de error."""

from enum import Enum, auto


class TipoOperacion(Enum):
    """Tipo de operación de persistencia."""
    LECTURA = auto()
    ESCRITURA = auto()

# ==============================================================================
# ARCHIVO 21/43: persistencia_exception.py
# Directorio: src/excepciones
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/persistencia_exception.py
# ==============================================================================

from enum import Enum
from src.excepciones.forestacion_exception import ForestacionException

class TipoOperacion(Enum):
    """Tipos de operaciones de persistencia"""
    LECTURA = "LECTURA"
    ESCRITURA = "ESCRITURA"

class PersistenciaException(ForestacionException):
    """Excepción lanzada cuando hay problemas de persistencia"""

    def __init__(self, tipo_operacion: TipoOperacion, nombre_archivo: str, mensaje: str):
        super().__init__("ERR_PERS", mensaje)
        self._tipo_operacion = tipo_operacion
        self._nombre_archivo = nombre_archivo

    @staticmethod
    def from_io_exception(tipo_operacion: TipoOperacion, nombre_archivo: str, e: Exception) -> 'PersistenciaException':
        return PersistenciaException(
            tipo_operacion,
            nombre_archivo,
            f"Error de E/S en {tipo_operacion.value}: {str(e)}"
        )

    @staticmethod
    def from_class_not_found_exception(nombre_archivo: str) -> 'PersistenciaException':
        return PersistenciaException(
            TipoOperacion.LECTURA,
            nombre_archivo,
            "Error de deserialización: Clase no encontrada"
        )

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

# ==============================================================================
# ARCHIVO 22/43: superficie_insuficiente_exception.py
# Directorio: src/excepciones
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from src.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie para plantar"""

    def __init__(self, tipo_cultivo: str, superficie_requerida: float, superficie_disponible: float):
        message = (f"Superficie insuficiente para plantar {tipo_cultivo}. "
                  f"Requerida: {superficie_requerida} m², "
                  f"Disponible: {superficie_disponible} m²")
        super().__init__("ERR_SUP", message)
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible


################################################################################
# DIRECTORIO: src/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 23/43: cultivo_factory.py
# Directorio: src/patrones/factory
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/factory/cultivo_factory.py
# ==============================================================================

from typing import Dict, Type, Callable, Optional
from src.entidades.cultivos.cultivo import Cultivo
from src.entidades.cultivos.pino import Pino
from src.entidades.cultivos.olivo import Olivo
from src.entidades.cultivos.lechuga import Lechuga
from src.entidades.cultivos.zanahoria import Zanahoria
from src.entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """Factory Method para crear diferentes tipos de cultivos"""

    # Constantes de cultivos
    SUPERFICIE_PINO = 2.0  # m²
    AGUA_INICIAL_PINO = 2  # litros
    ALTURA_INICIAL_ARBOL = 1.0  # metros

    SUPERFICIE_OLIVO = 3.0  # m²
    AGUA_INICIAL_OLIVO = 5  # litros
    ALTURA_INICIAL_OLIVO = 0.5  # metros

    SUPERFICIE_LECHUGA = 0.10  # m²
    AGUA_INICIAL_LECHUGA = 1  # litros

    SUPERFICIE_ZANAHORIA = 0.15  # m²
    AGUA_INICIAL_ZANAHORIA = 0  # litros

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """Crea un cultivo basado en su especie"""
        factories: Dict[str, Callable[[], Cultivo]] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie de cultivo no válida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        return Pino(
            agua=CultivoFactory.AGUA_INICIAL_PINO,
            altura=CultivoFactory.ALTURA_INICIAL_ARBOL,
            superficie=CultivoFactory.SUPERFICIE_PINO,
            variedad="Parana"
        )

    @staticmethod
    def _crear_olivo() -> Olivo:
        return Olivo(
            agua=CultivoFactory.AGUA_INICIAL_OLIVO,
            altura=CultivoFactory.ALTURA_INICIAL_OLIVO,
            superficie=CultivoFactory.SUPERFICIE_OLIVO,
            tipo_aceituna=TipoAceituna.ARBEQUINA
        )

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        return Lechuga(
            agua=CultivoFactory.AGUA_INICIAL_LECHUGA,
            superficie=CultivoFactory.SUPERFICIE_LECHUGA,
            variedad="Crespa"
        )

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        return Zanahoria(
            agua=CultivoFactory.AGUA_INICIAL_ZANAHORIA,
            superficie=CultivoFactory.SUPERFICIE_ZANAHORIA,
            is_baby_carrot=False
        )


################################################################################
# DIRECTORIO: src/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 24/43: observable.py
# Directorio: src/patrones/observer
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/observer/observable.py
# ==============================================================================

from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para observadores de eventos genéricos"""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Recibe y procesa una actualización de evento"""
        pass

class Observable(Generic[T], ABC):
    """Clase base para objetos observables genéricos"""

    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un nuevo observador"""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador existente"""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados"""
        for observador in self._observadores:
            observador.actualizar(evento)


################################################################################
# DIRECTORIO: src/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 25/43: absorcion_agua_strategy.py
# Directorio: src/patrones/strategy
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Estrategia abstracta para el cálculo de absorción de agua"""

    @abstractmethod
    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Calcula la cantidad de agua que absorberá el cultivo"""
        pass

# ==============================================================================
# ARCHIVO 26/43: absorcion_constante_strategy.py
# Directorio: src/patrones/strategy
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_constante_strategy.py
# ==============================================================================

from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante para hortalizas"""

    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Retorna una cantidad constante de absorción"""
        return self._cantidad

# ==============================================================================
# ARCHIVO 27/43: absorcion_seasonal_strategy.py
# Directorio: src/patrones/strategy
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/patrones/strategy/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from src.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from src.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción estacional para árboles"""

    # Constantes para absorción estacional
    ABSORCION_SEASONAL_VERANO = 5  # L
    ABSORCION_SEASONAL_INVIERNO = 2  # L
    MES_INICIO_VERANO = 3  # marzo
    MES_FIN_VERANO = 8  # agosto

    def calcular_absorcion(self, cultivo: Cultivo) -> int:
        """Calcula absorción según la estación"""
        mes_actual = date.today().month
        if self.MES_INICIO_VERANO <= mes_actual <= self.MES_FIN_VERANO:
            return self.ABSORCION_SEASONAL_VERANO
        return self.ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: src/riego/control
################################################################################

# ==============================================================================
# ARCHIVO 28/43: control_riego_task.py
# Directorio: src/riego/control
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from src.patrones.observer.observable import Observer
from src.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from src.riego.sensores.humedad_reader_task import HumedadReaderTask
from src.entidades.terrenos.plantacion import Plantacion
from src.servicios.terrenos.plantacion_service import PlantacionService
from src.excepciones.agua_agotada_exception import AguaAgotadaException

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador de riego automático basado en sensores"""

    # Constantes de control
    INTERVALO_CONTROL = 2.5  # segundos
    TEMP_MIN_RIEGO = 8.0  # °C
    TEMP_MAX_RIEGO = 15.0  # °C
    HUMEDAD_MAX_RIEGO = 50.0  # %

    def __init__(self, sensor_temperatura: TemperaturaReaderTask,
                 sensor_humedad: HumedadReaderTask,
                 plantacion: Plantacion,
                 plantacion_service: PlantacionService):
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        self._ultima_temperatura = sensor_temperatura.get_ultima_temperatura()
        self._ultima_humedad = sensor_humedad.get_ultima_humedad()

        # Suscribirse a los sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def detener(self) -> None:
        """Detiene la tarea de control"""
        self._detenido.set()
        self._sensor_temperatura.eliminar_observador(self)
        self._sensor_humedad.eliminar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Recibe actualizaciones de los sensores"""
        if isinstance(self._sensor_temperatura, TemperaturaReaderTask):
            self._ultima_temperatura = evento
        else:
            self._ultima_humedad = evento

    def run(self) -> None:
        """Ejecuta el control de riego"""
        while not self._detenido.is_set():
            try:
                # Verificar condiciones de riego
                if (self.TEMP_MIN_RIEGO <= self._ultima_temperatura <= self.TEMP_MAX_RIEGO and
                    self._ultima_humedad < self.HUMEDAD_MAX_RIEGO):
                    # Condiciones óptimas - regar
                    self._plantacion_service.regar(self._plantacion)
            except AguaAgotadaException:
                print("Control de riego detenido: agua agotada")
                self.detener()
            finally:
                time.sleep(self.INTERVALO_CONTROL)


################################################################################
# DIRECTORIO: src/riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 29/43: humedad_reader_task.py
# Directorio: src/riego/sensores
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import random
import time
from src.patrones.observer.observable import Observable

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Tarea que lee humedad en segundo plano y notifica a observadores"""

    # Constantes del sensor
    INTERVALO_SENSOR = 3.0  # segundos
    HUMEDAD_MIN = 0.0  # %
    HUMEDAD_MAX = 100.0  # %

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_humedad = 50.0  # humedad inicial por defecto

    def detener(self) -> None:
        """Detiene la tarea de lectura"""
        self._detenido.set()

    def run(self) -> None:
        """Ejecuta la tarea de lectura continua"""
        while not self._detenido.is_set():
            self._ultima_humedad = self._leer_humedad()
            self.notificar_observadores(self._ultima_humedad)
            time.sleep(self.INTERVALO_SENSOR)

    def _leer_humedad(self) -> float:
        """Simula la lectura del sensor de humedad"""
        return random.uniform(self.HUMEDAD_MIN, self.HUMEDAD_MAX)

    def get_ultima_humedad(self) -> float:
        """Retorna la última humedad leída"""
        return self._ultima_humedad

# ==============================================================================
# ARCHIVO 30/43: temperatura_reader_task.py
# Directorio: src/riego/sensores
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import random
import time
from src.patrones.observer.observable import Observable

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Tarea que lee temperatura en segundo plano y notifica a observadores"""

    # Constantes del sensor
    INTERVALO_SENSOR = 2.0  # segundos
    TEMP_MIN = -25.0  # °C
    TEMP_MAX = 50.0  # °C

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._ultima_temperatura = 20.0  # temperatura inicial por defecto

    def detener(self) -> None:
        """Detiene la tarea de lectura"""
        self._detenido.set()

    def run(self) -> None:
        """Ejecuta la tarea de lectura continua"""
        while not self._detenido.is_set():
            self._ultima_temperatura = self._leer_temperatura()
            self.notificar_observadores(self._ultima_temperatura)
            time.sleep(self.INTERVALO_SENSOR)

    def _leer_temperatura(self) -> float:
        """Simula la lectura del sensor de temperatura"""
        return random.uniform(self.TEMP_MIN, self.TEMP_MAX)

    def get_ultima_temperatura(self) -> float:
        """Retorna la última temperatura leída"""
        return self._ultima_temperatura


################################################################################
# DIRECTORIO: src/servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 31/43: arbol_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/arbol_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 32/43: cultivo_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/cultivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 33/43: cultivo_service_registry.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 34/43: lechuga_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/lechuga_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 35/43: olivo_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/olivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 36/43: pino_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/pino_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 37/43: zanahoria_service.py
# Directorio: src/servicios/cultivos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/cultivos/zanahoria_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: src/servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 38/43: fincas_service.py
# Directorio: src/servicios/negocio
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/negocio/fincas_service.py
# ==============================================================================

"""Servicio central para gestión de múltiples fincas."""

from typing import Dict, Type, TypeVar

from src.entidades.terrenos.registro_forestal import RegistroForestal
from src.servicios.negocio.paquete import Paquete

T = TypeVar('T')

class FincasService:
    """Servicio para gestión de múltiples fincas."""

    def __init__(self):
        """Inicializa diccionario interno de fincas."""
        self._fincas: Dict[int, RegistroForestal] = {}

    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al servicio.
        
        Args:
            registro: Registro forestal a agregar
        """
        self._fincas[registro.get_id_padron()] = registro
        print(f"Finca de {registro.get_propietario()} agregada exitosamente")

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por su padrón.
        
        Args:
            id_padron: ID de padrón catastral
            
        Returns:
            Registro forestal encontrado
            
        Raises:
            KeyError: Si no existe finca con ese padrón
        """
        if id_padron not in self._fincas:
            raise KeyError(f"No existe finca con padrón {id_padron}")
        return self._fincas[id_padron]

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca con plaguicida específico.
        
        Args:
            id_padron: ID de padrón catastral
            plaguicida: Tipo de plaguicida a aplicar
            
        Raises:
            KeyError: Si no existe finca con ese padrón
        """
        finca = self.buscar_finca(id_padron)
        print(f"\nFumigando plantación con: {plaguicida}")

    def cosechar_y_empaquetar(self, tipo: Type[T]) -> Paquete[T]:
        """
        Cosecha cultivos de un tipo y los empaqueta.
        
        Args:
            tipo: Tipo de cultivo a cosechar
            
        Returns:
            Paquete con cultivos cosechados
        """
        paquete = Paquete[T](tipo)
        cantidad = 0

        # Cosechar de todas las fincas
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cultivos = plantacion.get_cultivos()
            
            # Remover cultivos del tipo especificado
            cultivos_tipo = [c for c in cultivos if isinstance(c, tipo)]
            for cultivo in cultivos_tipo:
                plantacion.remove_cultivo(cultivo)
                paquete.agregar(cultivo)
                cantidad += 1

        print(f"\nCOSECHANDO {cantidad} unidades de {tipo}")
        paquete.mostrar_contenido_caja()
        return paquete

# ==============================================================================
# ARCHIVO 39/43: paquete.py
# Directorio: src/servicios/negocio
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/negocio/paquete.py
# ==============================================================================

"""Servicio de alto nivel para gestión de múltiples fincas."""

from typing import Dict, Type, TypeVar, Generic
from src.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

T = TypeVar('T')

class Paquete(Generic[T]):
    """Contenedor genérico tipo-seguro para cultivos cosechados."""

    def __init__(self, tipo: Type[T]):
        self._tipo = tipo
        self._items: list[T] = []
        self._id = Paquete._siguiente_id
        Paquete._siguiente_id += 1

    def agregar(self, item: T) -> None:
        """Agrega un item al paquete."""
        self._items.append(item)

    def get_items(self) -> list[T]:
        """Retorna copia de la lista de items."""
        return self._items.copy()

    def mostrar_contenido_caja(self) -> None:
        """Muestra contenido del paquete."""
        print(f"\nContenido de la caja:")
        print(f"  Tipo: {self._tipo.__name__}")
        print(f"  Cantidad: {len(self._items)}")
        print(f"  ID Paquete: {self._id}")

    _siguiente_id = 1  # ID autoincremental para paquetes


################################################################################
# DIRECTORIO: src/servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 40/43: trabajador_service.py
# Directorio: src/servicios/personal
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/personal/trabajador_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: src/servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 41/43: plantacion_service.py
# Directorio: src/servicios/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/plantacion_service.py
# ==============================================================================

"""Servicio para gestión de plantaciones."""

from typing import List, TYPE_CHECKING

from src.patrones.factory.cultivo_factory import CultivoFactory
from src.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from src.excepciones.agua_agotada_exception import AguaAgotadaException

if TYPE_CHECKING:
    from src.entidades.terrenos.plantacion import Plantacion
    from src.entidades.cultivos.cultivo import Cultivo


class PlantacionService:
    """Servicio de gestión de plantaciones."""

    def plantar(
        self,
        plantacion: 'Plantacion',
        especie: str,
        cantidad: int
    ) -> None:
        """
        Planta múltiples cultivos de una especie.
        
        Args:
            plantacion: Plantación donde plantar
            especie: Tipo de cultivo a plantar
            cantidad: Cantidad de cultivos a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay espacio
            ValueError: Si especie no existe
        """
        # Crear cultivos vía Factory
        cultivos: List['Cultivo'] = []
        superficie_requerida = 0

        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            cultivos.append(cultivo)
            superficie_requerida += cultivo.get_superficie()

        # Verificar superficie
        if superficie_requerida > plantacion.get_superficie_disponible():
            raise SuperficieInsuficienteException(
                superficie_requerida,
                plantacion.get_superficie_disponible()
            )

        # Agregar cultivos
        for cultivo in cultivos:
            plantacion.add_cultivo(cultivo)

        print(f"{cantidad} {especie}(s) plantado(s) exitosamente")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de una plantación.
        
        Args:
            plantacion: Plantación a regar
            
        Raises:
            AguaAgotadaException: Si no hay suficiente agua
        """
        if plantacion.get_agua_disponible() < 10:
            raise AguaAgotadaException()

        # Consumir agua de plantación
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - 10)

        # Regar cada cultivo
        for cultivo in plantacion.get_cultivos():
            from src.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
            registry = CultivoServiceRegistry.get_instance()
            agua_absorbida = registry.absorber_agua(cultivo)
            print(f"{type(cultivo).__name__} absorbió {agua_absorbida}L de agua")

# ==============================================================================
# ARCHIVO 42/43: registro_forestal_service.py
# Directorio: src/servicios/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

"""Servicio de persistencia de registros forestales."""

import os
import pickle
from typing import TYPE_CHECKING

from src.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from src.excepciones.persistencia_exception import PersistenciaException
from src.excepciones.mensajes_exception import TipoOperacion

if TYPE_CHECKING:
    from src.entidades.terrenos.registro_forestal import RegistroForestal


class RegistroForestalService:
    """Servicio para persistencia de registros forestales."""

    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Persiste un registro forestal en disco.
        
        Args:
            registro: Registro a persistir
        
        Raises:
            PersistenciaException: Si hay error al persistir
        """
        # Crear directorio data si no existe
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        nombre_archivo = f"{DIRECTORIO_DATA}/{registro.get_propietario()}{EXTENSION_DATA}"
        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente "
                  f"en {nombre_archivo}")
        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al persistir registro de {registro.get_propietario()}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion=TipoOperacion.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """
        Lee un registro forestal desde disco.
        
        Args:
            propietario: Nombre del propietario del registro a leer
        
        Returns:
            RegistroForestal recuperado
            
        Raises:
            ValueError: Si propietario es vacío
            PersistenciaException: Si hay error al leer
        """
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")

        nombre_archivo = f"{DIRECTORIO_DATA}/{propietario}{EXTENSION_DATA}"
        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(f"Registro de {propietario} recuperado exitosamente desde "
                  f"{nombre_archivo}")
            return registro
        except FileNotFoundError:
            raise PersistenciaException(
                user_message=f"No existe registro para {propietario}",
                technical_message="Archivo no encontrado",
                nombre_archivo=nombre_archivo,
                tipo_operacion=TipoOperacion.LECTURA
            )
        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al leer registro de {propietario}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion=TipoOperacion.LECTURA
            )

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """
        Muestra datos completos de un registro forestal.
        
        Args:
            registro: Registro a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padrón:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avalúo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie()}")
        print(f"Cantidad de cultivos plantados: "
              f"{len(registro.get_plantacion().get_cultivos())}\n")
        print("Listado de Cultivos plantados")
        print("____________________________\n")

        from src.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
        registry = CultivoServiceRegistry.get_instance()

        for cultivo in registro.get_plantacion().get_cultivos():
            registry.mostrar_datos(cultivo)
            print()

# ==============================================================================
# ARCHIVO 43/43: tierra_service.py
# Directorio: src/servicios/terrenos
# Ruta completa: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/tierra_service.py
# ==============================================================================

"""Servicio para gestión de terrenos."""

from typing import TYPE_CHECKING

from src.entidades.terrenos.tierra import Tierra
from src.entidades.terrenos.plantacion import Plantacion
from src.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from src.entidades.cultivos.cultivo import Cultivo


class TierraService:
    """Servicio de gestión de terrenos."""

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con una plantación.
        
        Args:
            id_padron_catastral: ID del padrón
            superficie: Superficie en m²
            domicilio: Domicilio del terreno
            nombre_plantacion: Nombre de la plantación
            
        Returns:
            Terreno creado con plantación
            
        Raises:
            ValueError: Si superficie <= 0
        """
        # Validar superficie
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")

        # Crear terreno
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        print(f"\nTerreno creado:")
        print(f"  Padrón: {id_padron_catastral}")
        print(f"  Superficie: {superficie} m²")
        print(f"  Domicilio: {domicilio}")

        # Crear plantación
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )
        print(f"\nPlantación creada:")
        print(f"  Nombre: {nombre_plantacion}")
        print(f"  Agua inicial: {AGUA_INICIAL_PLANTACION}L")

        # Vincular plantación a terreno
        tierra.set_finca(plantacion)
        return tierra


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 43
# Generado: 2025-10-22 01:14:01
################################################################################
