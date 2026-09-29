#aplicaion
from aplicacion.puertos.notificador import Notificador
from aplicacion.puertos.proveedor_fecha import ProveedorFecha
from aplicacion.puertos.repo_equipo import RepoEquipo
from aplicacion.puertos.repo_estudiante import RepoEstudiante
from aplicacion.puertos.repo_prestamo import RepoPrestamo

#dominio
from dominio.calculadora_multa import CalculadoraMulta
from dominio.equipo import Equipo
from dominio.estado_entrega import EstadoEntrega
from dominio.excepciones import EquipoNoEncontrado
from dominio.excepciones import PrestamoNoEncontrado
from dominio.prestamo import Prestamo

class RegistrarDevolucion:

    def __init__(self, repo_prestamo: RepoPrestamo, repo_equipo: RepoEquipo, repo_estudiante: RepoEstudiante, proveedor_fecha: ProveedorFecha,
                 notificador: Notificador):
        self._repo_prestamo = repo_prestamo
        self._repo_equipo = repo_equipo
        self._repo_estudiante = repo_estudiante
        self._proveedor_fecha = proveedor_fecha
        self._notificador = notificador
        self._calculadora_multa = CalculadoraMulta()

    def ejecutar(self, prestamo_id: int, condicion: EstadoEntrega) -> Prestamo:
        prestamo = self._buscar_prestamo(prestamo_id)
        equipo = self._buscar_equipo(prestamo.codigo_equipo)
        fecha_entrega = self._proveedor_fecha.hoy()
        multa = self._calculadora_multa.calcular(
            prestamo.fecha_limite, fecha_entrega, equipo.categoria
        )
        prestamo.cerrar(fecha_entrega, multa)
        equipo.recibir(condicion)
        self._repo_prestamo.guardar_prestamo(prestamo)
        self._repo_equipo.guardar_equipo(equipo)
        self._cobrar_multa(prestamo)
        return prestamo

    def _buscar_prestamo(self, prestamo_id: int) -> Prestamo:
        prestamo = self._repo_prestamo.buscar_prestamo(prestamo_id)
        if prestamo is None:
            raise PrestamoNoEncontrado(prestamo_id)
        return prestamo

    def _buscar_equipo(self, codigo: str) -> Equipo:
        equipo = self._repo_equipo.buscar_equipo(codigo)
        if equipo is None:
            raise EquipoNoEncontrado(codigo)
        return equipo

    def _cobrar_multa(self, prestamo: Prestamo) -> None:
        if prestamo.multa == CalculadoraMulta.SIN_MULTA:
            return
        estudiante = self._repo_estudiante.buscar_estudiante(prestamo.estudiante_id)
        estudiante.adicionar_multa(prestamo.multa)
        self._repo_estudiante.guardar_estudiante(estudiante)
        self._notificador.notificar_multa(prestamo.estudiante_id, prestamo)
        