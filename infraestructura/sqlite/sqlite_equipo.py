from aplicacion.puertos.repo_equipo import RepoEquipo
from dominio.catalogo_categorias import CatalogoCategorias
from dominio.equipo import Equipo
from dominio.estado_equipo import EstadoEquipo
from infraestructura.sqlite.conexion_sqlite import ConexionSqlite


class SQLiteEquipo(RepoEquipo):
    """Guarda y busca equipos en la tabla equipos de SQLite."""

    def __init__(self, conexion_sqlite: ConexionSqlite, catalogo: CatalogoCategorias):
        self._conexion = conexion_sqlite.conexion
        self._catalogo = catalogo

    def guardar_equipo(self, equipo: Equipo) -> None:
        self._conexion.execute(
            "INSERT INTO equipos (codigo, categoria, estado) VALUES (?, ?, ?) "
            "ON CONFLICT (codigo) DO UPDATE SET "
            "categoria = excluded.categoria, estado = excluded.estado",
            (equipo.codigo, equipo.categoria.nombre(), equipo.estado.value),
        )
        self._conexion.commit()

    def buscar_equipo(self, codigo: str) -> Equipo | None:
        fila = self._conexion.execute(
            "SELECT codigo, categoria, estado FROM equipos WHERE codigo = ?",
            (codigo,),
        ).fetchone()
        if fila is None:
            return None
        codigo_guardado, nombre_categoria, estado = fila
        categoria = self._catalogo.obtener(nombre_categoria)
        return Equipo(codigo_guardado, categoria, EstadoEquipo(estado))
