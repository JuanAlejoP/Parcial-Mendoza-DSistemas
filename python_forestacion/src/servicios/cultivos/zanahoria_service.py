from src.servicios.cultivos.cultivo_service import CultivoService
from src.entidades.cultivos.zanahoria import Zanahoria
from src.patrones.strategy.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    """Servicio específico para zanahorias"""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))  # 2L constante

    def mostrar_datos(self, zanahoria: Zanahoria) -> None:
        tipo = "Baby carrot" if zanahoria.is_baby_carrot() else "Regular"
        print(f"Cultivo: Zanahoria\n"
              f"Superficie: {zanahoria.get_superficie()} m²\n"
              f"Agua almacenada: {zanahoria.get_agua()} L\n"
              f"Tipo: {tipo}\n"
              f"Invernadero: {zanahoria.get_requiere_invernadero()}\n")