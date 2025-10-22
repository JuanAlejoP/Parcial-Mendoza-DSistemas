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