from src.servicios.cultivos.cultivo_service import CultivoService
from src.entidades.cultivos.lechuga import Lechuga
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class LechugaService(CultivoService):
    """Servicio específico para lechugas"""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))  # 1L constante

    def mostrar_datos(self, lechuga: Lechuga) -> None:
        print(f"Cultivo: Lechuga\n"
              f"Superficie: {lechuga.get_superficie()} m²\n"
              f"Agua almacenada: {lechuga.get_agua()} L\n"
              f"Variedad: {lechuga.get_variedad()}\n"
              f"Invernadero: {lechuga.get_requiere_invernadero()}\n")