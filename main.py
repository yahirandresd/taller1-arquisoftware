from datetime import date

from aplicacion.casos_uso.registrar_devolucion import RegistrarDevolucion
from aplicacion.casos_uso.registrar_prestamo import RegistrarPrestamo
from dominio.catalogo_categorias import CatalogoCategorias
from dominio.categorias.categoria_camara import CategoriaCamara
from dominio.categorias.categoria_kit_robotica import CategoriaKitRobotica
from dominio.categorias.categoria_portatil import CategoriaPortatil
from dominio.categorias.categoria_proyector import CategoriaProyector
from dominio.equipo import Equipo
from dominio.estado_entrega import EstadoEntrega
from dominio.estudiantes import Estudiantes
from dominio.excepciones import ErrorDominio
from dominio.prestamo import Prestamo
from infraestructura.sqlite.conexion_sqlite import ConexionSqlite
from infraestructura.fecha.fecha_fija import FechaFija
from infraestructura.memoria.memoria_prestamo import MemoriaPrestamo
from infraestructura.notificacion.notificador_consola import NotificadorConsola
from infraestructura.sqlite.sqlite_equipo import SQLiteEquipo
from infraestructura.sqlite.sqlite_estudiantes import SQLiteEstudiantes
from infraestructura.sqlite.sqlite_prestamo import SQLitePrestamo

FECHA_DEMO = date(2026, 10, 5)
FECHA_DEVOLUCION_CA3 = date(2026, 10, 6)


class Main:
    """Punto de arranque: arma el sistema y ejecuta los casos de aceptación.

    Es el único archivo que conoce las clases concretas de infraestructura.
    """

    def __init__(self):
        self.catalogo = CatalogoCategorias()
        self.catalogo.registrar(CategoriaPortatil())
        self.catalogo.registrar(CategoriaCamara())
        self.catalogo.registrar(CategoriaKitRobotica())
        self.catalogo.registrar(CategoriaProyector())  

    def componer(self, fecha_hoy: date) -> None:
        #Crea una base de datos vacía y conecta los casos de uso con sus adaptadores
        conexion = ConexionSqlite(":memory:")
        conexion.crear_tablas()
        self.repo_estudiante = SQLiteEstudiantes(conexion)
        self.repo_equipo = SQLiteEquipo(conexion, self.catalogo)
        self.repo_prestamo = SQLitePrestamo(conexion)
        
        # LSP: cambiar solo la línea anterior por la de abajo y el demo da el mismo resultado
        # self.repo_prestamo = MemoriaPrestamo()
        self._crear_casos_de_uso(FechaFija(fecha_hoy), NotificadorConsola())

    def _crear_casos_de_uso(self, proveedor_fecha: FechaFija,
                            notificador: NotificadorConsola) -> None:
        self.registrar_prestamo = RegistrarPrestamo(
            self.repo_estudiante, self.repo_equipo, self.repo_prestamo,
            proveedor_fecha, notificador)
        self.registrar_devolucion = RegistrarDevolucion(
            self.repo_prestamo, self.repo_equipo, self.repo_estudiante,
            proveedor_fecha, notificador)

    def modo_demo(self) -> None:
        self.ca1_prestamo_exitoso()
        self.ca2_limite_de_prestamos()
        self.ca3_devolucion_con_multa()
        self.ca4_estudiante_con_multa()
        self.ca5_devolucion_con_dano()
        self.ca6_categoria_proyector()

    #casos de aceptación -------------------------

    def ca1_prestamo_exitoso(self) -> None:
        self._titulo("CA1: Ana sin préstamos pide PORTATIL-01")
        self.componer(FECHA_DEMO)
        self._crear_estudiante("ana", "Ana", "Gómez")
        self._crear_equipo("PORTATIL-01", CategoriaPortatil.NOMBRE)
        prestamo = self.registrar_prestamo.ejecutar("ana", "PORTATIL-01")
        print(f"Préstamo {prestamo.id} creado. Fecha límite: {prestamo.fecha_limite}")

    def ca2_limite_de_prestamos(self) -> None:
        self._titulo("CA2: Ana con 2 préstamos activos pide un tercer equipo")
        self.componer(FECHA_DEMO)
        self._crear_estudiante("ana", "Ana", "Gómez")
        self._crear_prestamo_activo("ana", "PORTATIL-01", CategoriaPortatil.NOMBRE, FECHA_DEMO)
        self._crear_prestamo_activo("ana", "CAMARA-01", CategoriaCamara.NOMBRE, FECHA_DEMO)
        self._crear_equipo("KIT-01", CategoriaKitRobotica.NOMBRE)
        self._intentar_prestamo("ana", "KIT-01")

    def ca3_devolucion_con_multa(self) -> None:
        self._titulo("CA3: CAMARA-02 prestada el 2026-10-01 y devuelta el 2026-10-06")
        self.componer(FECHA_DEVOLUCION_CA3)
        self._crear_estudiante("ana", "Ana", "Gómez")
        prestamo = self._crear_prestamo_activo(
            "ana", "CAMARA-02", CategoriaCamara.NOMBRE, date(2026, 10, 1))
        devuelto = self.registrar_devolucion.ejecutar(prestamo.id, EstadoEntrega.SIN_DANO)
        multa = f"{devuelto.multa:,}".replace(",", ".")
        print(f"Fecha límite: {devuelto.fecha_limite}. Multa generada: ${multa}")

    def ca4_estudiante_con_multa(self) -> None:
        self._titulo("CA4: Luis con multa pendiente pide un equipo")
        self.componer(FECHA_DEMO)
        self._crear_estudiante("luis", "Luis", "Pérez", multa_pendiente=8_000)
        self._crear_equipo("PORTATIL-02", CategoriaPortatil.NOMBRE)
        self._intentar_prestamo("luis", "PORTATIL-02")

    def ca5_devolucion_con_dano(self) -> None:
        self._titulo("CA5: un equipo se devuelve con daño")
        self.componer(FECHA_DEMO)
        self._crear_estudiante("ana", "Ana", "Gómez")
        self._crear_estudiante("luis", "Luis", "Pérez")
        prestamo = self._crear_prestamo_activo(
            "ana", "KIT-02", CategoriaKitRobotica.NOMBRE, FECHA_DEMO)
        self.registrar_devolucion.ejecutar(prestamo.id, EstadoEntrega.CON_DANO)
        estado = self.repo_equipo.buscar_equipo("KIT-02").estado
        print(f"Estado de KIT-02 después de la devolución: {estado.value}")
        self._intentar_prestamo("luis", "KIT-02")

    def ca6_categoria_proyector(self) -> None:
        self._titulo("CA6: préstamo de un equipo de la nueva categoría PROYECTOR")
        self.componer(FECHA_DEMO)
        self._crear_estudiante("carlos", "Carlos", "Soto")
        self._crear_equipo("PROYECTOR-01", CategoriaProyector.NOMBRE)
        prestamo = self.registrar_prestamo.ejecutar("carlos", "PROYECTOR-01")
        print(f"Préstamo {prestamo.id} creado. Fecha límite: {prestamo.fecha_limite}")

    # --------------------------- datos iniciales ---------------------------

    def _crear_estudiante(self, estudiante_id: str, nombres: str, apellidos: str,
                          multa_pendiente: int = 0) -> None:
        correo = f"{estudiante_id}@universidad.edu.co"
        estudiante = Estudiantes(estudiante_id, nombres, apellidos, correo,
                                 "3000000000", multa_pendiente)
        self.repo_estudiante.guardar_estudiante(estudiante)

    def _crear_equipo(self, codigo: str, nombre_categoria: str) -> Equipo:
        equipo = Equipo(codigo, self.catalogo.obtener(nombre_categoria))
        self.repo_equipo.guardar_equipo(equipo)
        return equipo

    def _crear_prestamo_activo(self, estudiante_id: str, codigo: str,
                               nombre_categoria: str, fecha_inicio: date) -> Prestamo:
        equipo = self._crear_equipo(codigo, nombre_categoria)
        equipo.marcar_prestado()
        self.repo_equipo.guardar_equipo(equipo)
        fecha_limite = equipo.categoria.fecha_limite_desde(fecha_inicio)
        prestamo = Prestamo(None, estudiante_id, codigo, fecha_inicio, fecha_limite)
        self.repo_prestamo.guardar_prestamo(prestamo)
        return prestamo

    # utilidades ------------------------------

    def _intentar_prestamo(self, estudiante_id: str, codigo_equipo: str) -> None:
        try:
            self.registrar_prestamo.ejecutar(estudiante_id, codigo_equipo)
            print("Préstamo creado (no se esperaba).")
        except ErrorDominio as error:
            print(f"Rechazado: {error}")

    def _titulo(self, texto: str) -> None:
        print()
        print("=" * 70)
        print(texto)
        print("=" * 70)


if __name__ == "__main__":
    Main().modo_demo()