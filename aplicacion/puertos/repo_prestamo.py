from abc import ABC, abstractmethod
from dominio.prestamo import Prestamo

class RepoPrestamo(ABC):

    @abstractmethod
    def guardar_prestamo(self, prestamo: Prestamo) -> None:
        """Si el préstamo no tiene id lo crea y se lo asigna; si ya lo tiene, lo actualiza."""

    @abstractmethod
    def buscar_prestamo(self, prestamo_id: int) -> Prestamo | None:
        """Devuelve el préstamo con ese id, o None si no existe."""

    @abstractmethod
    def buscar_activos_de_estudiante(self, estudiante_id: str) -> list[Prestamo]:
        """Devuelve los préstamos ACTIVOS del estudiante."""
