from aplicacion.puertos.repo_estudiante import RepoEstudiante
from dominio.estudiantes import Estudiantes
from infraestructura.sqlite.conexion_sqlite import ConexionSqlite


class SQLiteEstudiantes(RepoEstudiante):
    #Guarda y busca estudiantes en la tabla estudiantes de SQLite.

    COLUMNAS = "id, nombres, apellidos, correo, telefono, multa_pendiente"

    def __init__(self, conexion_sqlite: ConexionSqlite):
        self._conexion = conexion_sqlite.conexion

    def guardar_estudiante(self, estudiante: Estudiantes) -> None:
        self._conexion.execute(
            f"INSERT OR REPLACE INTO estudiantes ({self.COLUMNAS}) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (estudiante.id, estudiante.nombres, estudiante.apellidos,
             estudiante.correo, estudiante.telefono, estudiante.multa_pendiente),
        )
        self._conexion.commit()

    def buscar_estudiante(self, estudiante_id: str) -> Estudiantes | None:
        fila = self._conexion.execute(
            f"SELECT {self.COLUMNAS} FROM estudiantes WHERE id = ?",
            (estudiante_id,),
        ).fetchone()
        if fila is None:
            return None
        return Estudiantes(*fila)