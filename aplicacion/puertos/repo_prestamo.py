from abc import ABC, abstractmethod
from dominio.prestamo import Prestamo
from typing import List

class RepoPrestamo(ABC):
    @abstractmethod
    def guardarPrestamo(self, prestamo: Prestamo) -> None:
        pass

    @abstractmethod
    def buscarPrestActivEstud(self, estudiante_id: str) -> list[Prestamo]:
        pass

    