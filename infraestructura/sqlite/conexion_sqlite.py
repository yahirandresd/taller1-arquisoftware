import sqlite3

class ConexionSqlite:
    """Abre la base de datos SQLite y crea las tablas del sistema."""

    ESQUEMA = """
        CREATE TABLE IF NOT EXISTS estudiantes (
            id              TEXT PRIMARY KEY,
            nombres         TEXT NOT NULL,
            apellidos       TEXT NOT NULL,
            correo          TEXT,
            telefono        TEXT,
            multa_pendiente INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS equipos (
            codigo    TEXT PRIMARY KEY,
            categoria TEXT NOT NULL,
            estado    TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS prestamos (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id    TEXT NOT NULL REFERENCES estudiantes (id),
            codigo_equipo    TEXT NOT NULL REFERENCES equipos (codigo),
            fecha_inicio     TEXT NOT NULL,
            fecha_limite     TEXT NOT NULL,
            fecha_devolucion TEXT,
            estado           TEXT NOT NULL,
            multa            INTEGER NOT NULL DEFAULT 0
        );
    """

    def __init__(self, ruta_archivo: str = "laboratorio.db"):
        """Usa ":memory:" como ruta para una base de datos temporal y vacía."""
        self.conexion = sqlite3.connect(ruta_archivo)

    def crear_tablas(self) -> None:
        self.conexion.executescript(self.ESQUEMA)
        self.conexion.commit()

    def cerrar(self) -> None:
        self.conexion.close()
