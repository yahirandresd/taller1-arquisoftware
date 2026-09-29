from aplicacion.puertos.repo_prestamo import RepoPrestamo
from dominio.estado_prestamo import EstadoPrestamo
from dominio.prestamo import Prestamo

class MemoriaPrestamo(RepoPrestamo):
    """Guarda los préstamos en una lista; sustituye a SQLitePrestamo (LSP)."""

    def __init__(self):
        self._prestamos: list[Prestamo] = []
        self._siguiente_id = 1

    def guardar_prestamo(self, prestamo: Prestamo) -> None:
        if prestamo.id is None:
            self._insertar(prestamo)
        else:
            self._actualizar(prestamo)

    def buscar_prestamo(self, prestamo_id: int) -> Prestamo | None:
        for prestamo in self._prestamos:
            if prestamo.id == prestamo_id:
                return prestamo
        return None

    def buscar_activos_de_estudiante(self, estudiante_id: str) -> list[Prestamo]:
        return [prestamo for prestamo in self._prestamos
                if prestamo.estudiante_id == estudiante_id
                and prestamo.estado is EstadoPrestamo.ACTIVO]

    def _insertar(self, prestamo: Prestamo) -> None:
        prestamo.id = self._siguiente_id
        self._siguiente_id += 1
        self._prestamos.append(prestamo)

    def _actualizar(self, prestamo: Prestamo) -> None:
        for posicion, guardado in enumerate(self._prestamos):
            if guardado.id == prestamo.id:
                self._prestamos[posicion] = prestamo