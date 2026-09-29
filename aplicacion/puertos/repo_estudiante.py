from abc import ABC, abstractmethod
from dominio.estudiantes import Estudiantes

class RepoEstudiante(ABC):
    @abstractmethod
    def guardar_estudiante(self, estudiante: Estudiantes) -> None:
        ...
        
    @abstractmethod
    def buscar_estudiante(self, estudiante_id: str) -> Estudiantes | None:
        ...