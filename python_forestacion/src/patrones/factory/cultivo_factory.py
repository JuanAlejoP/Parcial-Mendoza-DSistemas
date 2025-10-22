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