from datetime import datetime
from dominio.prestamo import Prestamo
from dominio.excepciones import LimitePrestamoExcedido, EquipoNoDisponible, EstudianteConMultaActiva
from aplicacion.puertos.repo_prestamo import RepoPrestamo
from aplicacion.puertos.proveedor_fecha import ProveedorFecha

LIMITE_MAX_PRESTAMOS = 2

class RegistrarPrestamo:
    def __init__(self, repo_prestamo: RepoPrestamo, proveedor_fecha: ProveedorFecha):
        self.repo_prestamo = repo_prestamo
        self.proveedor_fecha = proveedor_fecha

    def registrar_prestamo(self, estudiante_id: str, codigo_equipo: str, estudiante_obj, equipo_obj, categoria_obj) -> Prestamo:
        # Verifica si estudiante tiene multas activas
        if estudiante_obj.tiene_multa_activa():
            raise EstudianteConMultaActiva()
        # verifica si equipo está disponible
        if not equipo_obj.esta_disponible():
            raise EquipoNoDisponible()
        activos = self.repo_prestamo.buscarPrestActivEstud(estudiante_id)
        # Verifica si el estudiante ha excedido el límite de préstamos
        if len(activos) >= LIMITE_MAX_PRESTAMOS:
            raise LimitePrestamoExcedido()
        fecha_in = self.proveedor_fecha.hoy()
        fecha_lim = categoria_obj.fecha_limite_desde(fecha_in)
        #guardar el prestamo nuevo
        nuevo = Prestamo(id=len(activos)+1, estudiante_id=estudiante_id, codigo_equipo=codigo_equipo, fecha_inicio=fecha_in, fecha_limite=fecha_lim)
        equipo_obj.marcar_prestado()
        self.repo_prestamo.guardarPrestamo(nuevo)
        return nuevo