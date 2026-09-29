from datetime import date

from aplicacion.puertos.repo_prestamo import RepoPrestamo
from dominio.estado_prestamo import EstadoPrestamo
from dominio.prestamo import Prestamo
from infraestructura.sqlite.conexion_sqlite import ConexionSqlite


class SQLitePrestamo(RepoPrestamo):
    """Guarda y busca préstamos en la tabla prestamos de SQLite."""

    COLUMNAS = ("id, estudiante_id, codigo_equipo, fecha_inicio, "
                "fecha_limite, fecha_devolucion, estado, multa")

    def __init__(self, conexion_sqlite: ConexionSqlite):
        self._conexion = conexion_sqlite.conexion

    def guardar_prestamo(self, prestamo: Prestamo) -> None:
        """Si el préstamo no tiene id lo crea; si ya lo tiene, lo actualiza."""
        if prestamo.id is None:
            self._insertar(prestamo)
        else:
            self._actualizar(prestamo)
        self._conexion.commit()

    def buscar_prestamo(self, prestamo_id: int) -> Prestamo | None:
        fila = self._conexion.execute(
            f"SELECT {self.COLUMNAS} FROM prestamos WHERE id = ?",
            (prestamo_id,),
        ).fetchone()
        if fila is None:
            return None
        return self._convertir_fila(fila)

    def buscar_activos_de_estudiante(self, estudiante_id: str) -> list[Prestamo]:
        filas = self._conexion.execute(
            f"SELECT {self.COLUMNAS} FROM prestamos "
            "WHERE estudiante_id = ? AND estado = ? ORDER BY id",
            (estudiante_id, EstadoPrestamo.ACTIVO.value),
        ).fetchall()
        return [self._convertir_fila(fila) for fila in filas]

    def _insertar(self, prestamo: Prestamo) -> None:
        cursor = self._conexion.execute(
            "INSERT INTO prestamos (estudiante_id, codigo_equipo, fecha_inicio, "
            "fecha_limite, fecha_devolucion, estado, multa) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (prestamo.estudiante_id, prestamo.codigo_equipo,
             prestamo.fecha_inicio.isoformat(), prestamo.fecha_limite.isoformat(),
             self._fecha_a_texto(prestamo.fecha_devolucion),
             prestamo.estado.value, prestamo.multa),
        )
        prestamo.id = cursor.lastrowid

    def _actualizar(self, prestamo: Prestamo) -> None:
        self._conexion.execute(
            "UPDATE prestamos SET fecha_devolucion = ?, estado = ?, multa = ? "
            "WHERE id = ?",
            (self._fecha_a_texto(prestamo.fecha_devolucion),
             prestamo.estado.value, prestamo.multa, prestamo.id),
        )

    def _convertir_fila(self, fila: tuple) -> Prestamo:
        return Prestamo(
            id=fila[0],
            estudiante_id=fila[1],
            codigo_equipo=fila[2],
            fecha_inicio=date.fromisoformat(fila[3]),
            fecha_limite=date.fromisoformat(fila[4]),
            fecha_devolucion=self._texto_a_fecha(fila[5]),
            estado=EstadoPrestamo(fila[6]),
            multa=fila[7],
        )

    def _fecha_a_texto(self, fecha: date | None) -> str | None:
        if fecha is None:
            return None
        return fecha.isoformat()

    def _texto_a_fecha(self, texto: str | None) -> date | None:
        if texto is None:
            return None
        return date.fromisoformat(texto)
