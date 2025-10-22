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