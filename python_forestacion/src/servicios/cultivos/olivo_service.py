from src.servicios.cultivos.arbol_service import ArbolService
from src.entidades.cultivos.olivo import Olivo
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class OlivoService(ArbolService):
    """Servicio específico para olivos"""

    # Constante para crecimiento
    INCREMENTO_ALTURA = 0.01  # metros por riego

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: Olivo) -> int:
        agua = super().absorver_agua(olivo)
        self.crecer(olivo, self.INCREMENTO_ALTURA)
        return agua

    def mostrar_datos(self, olivo: Olivo) -> None:
        print(f"Cultivo: Olivo\n"
              f"Superficie: {olivo.get_superficie()} m²\n"
              f"Agua almacenada: {olivo.get_agua()} L\n"
              f"ID: {olivo.get_id()}\n"
              f"Altura: {olivo.get_altura()} m\n"
              f"Tipo de aceituna: {olivo.get_tipo_aceituna().name}\n")