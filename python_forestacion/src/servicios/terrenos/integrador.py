"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: plantacion_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/3: registro_forestal_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/registro_forestal_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: tierra_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/terrenos/tierra_service.py
# ================================================================================

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

