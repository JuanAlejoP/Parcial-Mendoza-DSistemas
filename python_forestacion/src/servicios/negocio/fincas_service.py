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