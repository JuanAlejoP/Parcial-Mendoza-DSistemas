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