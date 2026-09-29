from abc import ABC, abstractmethod
from dominio.prestamo import Prestamo

class Notificador(ABC):
    #Puerto para avisar al estudiante -regla R7

    @abstractmethod
    def notificar_fecha_limite(self, estudiante_id: str, prestamo: Prestamo) -> None:
        """Avisa que se creó el préstamo y hasta cuándo debe devolverlo."""

    @abstractmethod
    def notificar_multa(self, estudiante_id: str, prestamo: Prestamo) -> None:
        """Avisa que la devolución generó una multa."""
