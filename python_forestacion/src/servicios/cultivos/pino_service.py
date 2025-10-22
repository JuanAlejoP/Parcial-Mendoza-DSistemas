from src.servicios.cultivos.arbol_service import ArbolService
from src.entidades.cultivos.pino import Pino
from src.patrones.strategy.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(ArbolService):
    """Servicio específico para pinos"""

    # Constante para crecimiento
    INCREMENTO_ALTURA = 0.10  # metros por riego

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: Pino) -> int:
        agua = super().absorver_agua(pino)
        self.crecer(pino, self.INCREMENTO_ALTURA)
        return agua

    def mostrar_datos(self, pino: Pino) -> None:
        print(f"Cultivo: Pino\n"
              f"Superficie: {pino.get_superficie()} m²\n"
              f"Agua almacenada: {pino.get_agua()} L\n"
              f"ID: {pino.get_id()}\n"
              f"Altura: {pino.get_altura()} m\n"
              f"Variedad: {pino.get_variedad()}\n")