from src.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base abstracta para hortalizas"""

    def __init__(self, agua: int, superficie: float, requiere_invernadero: bool):
        super().__init__(agua, superficie)
        self._requiere_invernadero = requiere_invernadero

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        super().set_agua(agua)