from abc import ABC, abstractmethod
from dominio.equipo import Equipo

class RepoEquipo(ABC):

    @abstractmethod
    def guardar_equipo(self, equipo: Equipo) -> None:
        """Crea el equipo o actualiza sus datos si ya existe."""

    @abstractmethod
    def buscar_equipo(self, codigo: str) -> Equipo | None:
        """Devuelve el equipo con ese código, o None si no existe."""
