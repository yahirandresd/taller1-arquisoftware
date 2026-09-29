from abc import ABC, abstractmethod
from datetime import date


class ProveedorFecha(ABC):
    """Puerto que entrega la fecha actual."""

    @abstractmethod
    def hoy(self) -> date:
        """Fecha de hoy según la implementación (real o fija)."""
