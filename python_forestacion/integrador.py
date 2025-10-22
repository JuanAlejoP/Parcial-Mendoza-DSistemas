"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: main.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/main.py
# ================================================================================

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

