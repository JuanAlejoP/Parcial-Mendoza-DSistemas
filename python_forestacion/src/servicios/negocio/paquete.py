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