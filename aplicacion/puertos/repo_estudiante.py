from abc import ABC, abstractmethod
from dominio.estudiantes import Estudiantes

class RepoEstudiante(ABC):
    @abstractmethod
    def guardarEstudiante(self, estudiante: Estudiantes) -> None:
        ...

    @abstractmethod
    def buscarEstudiantePorId(self, id: str) -> Estudiantes:
        ...