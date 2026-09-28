import sqlite3
from aplicacion.puertos.repo_estudiante import RepoEstudiante
from dominio.estudiantes import Estudiantes

class SQLiteEstudiantes(RepoEstudiante):
    def __init__(self, conexion):
        self.conn = conexion

    def guardarEstudiante(self, estudiante: Estudiantes) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO estudiantes VALUES (?, ?, ?, ?, ?, ?, ?)",
            (estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.correo, estudiante.telefono, estudiante.prest_activos, estudiante.multa_pend)
        )
        self.conn.commit()

    def buscarEstudianteporId(self, id: str) -> Estudiantes:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM estudiantes WHERE id = ?", (id,))
        fila = cursor.fetchone()
        return Estudiantes(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]) if fila else None

    