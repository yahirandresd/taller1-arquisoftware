#aplicacion
from aplicacion.puertos.notificador import Notificador
from aplicacion.puertos.proveedor_fecha import ProveedorFecha
from aplicacion.puertos.repo_equipo import RepoEquipo
from aplicacion.puertos.repo_estudiante import RepoEstudiante
from aplicacion.puertos.repo_prestamo import RepoPrestamo

#dominio
from dominio.equipo import Equipo
from dominio.estudiantes import Estudiantes
from dominio.excepciones import EquipoNoEncontrado
from dominio.excepciones import EstudianteConMultaActiva
from dominio.excepciones import LimitePrestamoExcedido
from dominio.prestamo import Prestamo

class RegistrarPrestamo:
    MAX_PRESTAMOS_ACTIVOS = 2

    def __init__(self, repo_estudiante: RepoEstudiante, repo_equipo: RepoEquipo, repo_prestamo: RepoPrestamo,
                 proveedor_fecha: ProveedorFecha, notificador: Notificador):
        self._repo_estudiante = repo_estudiante
        self._repo_equipo = repo_equipo
        self._repo_prestamo = repo_prestamo
        self._proveedor_fecha = proveedor_fecha
        self._notificador = notificador

    def ejecutar(self, estudiante_id: str, codigo_equipo: str) -> Prestamo:
        estudiante = self._repo_estudiante.buscar_estudiante(estudiante_id)
        equipo = self._buscar_equipo(codigo_equipo)
        self._validar_sin_multa(estudiante)
        self._validar_limite_prestamos(estudiante_id)
        equipo.marcar_prestado()
        prestamo = self._crear_prestamo(estudiante_id, equipo)
        self._repo_equipo.guardar_equipo(equipo)
        self._repo_prestamo.guardar_prestamo(prestamo)
        self._notificador.notificar_fecha_limite(estudiante_id, prestamo)
        return prestamo

    def _buscar_equipo(self, codigo: str) -> Equipo:
        equipo = self._repo_equipo.buscar_equipo(codigo)
        if equipo is None:
            raise EquipoNoEncontrado(codigo)
        return equipo

    def _validar_sin_multa(self, estudiante: Estudiantes) -> None:
        #regla R4
        if estudiante.tiene_multa_pendiente():
            raise EstudianteConMultaActiva()

    def _validar_limite_prestamos(self, estudiante_id: str) -> None:
        #regla R1
        activos = self._repo_prestamo.buscar_activos_de_estudiante(estudiante_id)
        if len(activos) >= self.MAX_PRESTAMOS_ACTIVOS:
            raise LimitePrestamoExcedido()

    def _crear_prestamo(self, estudiante_id: str, equipo: Equipo) -> Prestamo:
        #el plazo lo define la categoria - regla R3
        fecha_inicio = self._proveedor_fecha.hoy()
        fecha_limite = equipo.categoria.fecha_limite_desde(fecha_inicio)
        return Prestamo(None, estudiante_id, equipo.codigo, fecha_inicio, fecha_limite)
