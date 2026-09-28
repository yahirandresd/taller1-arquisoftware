from aplicacion.puertos.repo_prestamo import RepoPrestamo
from dominio.prestamo import Prestamo
from typing import List

class MemoriaPrestamo(RepoPrestamo):
    def __init__(self):
        self.almacenamiento: List[Prestamo] = []

    def guardarPrestamo(self, prestamo: Prestamo) -> None:
        prestamo.id = len(self.almacenamiento)+1  # Asigna un ID incremental basado en la longitud de la lista
        self.almacenamiento.append(prestamo)

    def buscarPrestActivEstud(self, estudiante_id: str) -> list[Prestamo]:
        return [prestamo for prestamo in self.almacenamiento if prestamo.estudiante_id == estudiante_id and prestamo.estado == "ACTIVO"]
    