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