"""
Archivo integrador generado automaticamente
Directorio: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/negocio
Fecha: 2025-10-22 01:14:01
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: fincas_service.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/negocio/fincas_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/2: paquete.py
# Ruta: /home/pupi/Escritorio/DSistemas/PARCIAL/python_forestacion/src/servicios/negocio/paquete.py
# ================================================================================

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

