from abc import ABC, abstractmethod
from datetime import date, timedelta


class Categoria(ABC):
    """Tipo de equipo, define el plazo del préstamo y la tarifa de multa."""

    @abstractmethod
    def nombre(self) -> str:
        """Nombre con el que la categoría se guarda en la bd"""

    @abstractmethod
    def dias_plazo(self) -> int:
        """Días que dura el préstamo - regla R3"""

    @abstractmethod
    def tarifa_diaria(self) -> int:
        """Pesos de multa por cada día completo de retraso - regla R5"""

    def fecha_limite_desde(self, fecha_inicio: date) -> date:
        #Calcula la fecha límite de devolución a desde del día del préstamo
        return fecha_inicio + timedelta(days=self.dias_plazo())
