class ErrorDominio(Exception):
    """Clase base de todos los errores de reglas de negocio."""


class CategoriaNoRegistrada(ErrorDominio):
    """Se pide una categoría que no fue registrada en el catálogo."""

    def __init__(self, nombre_categoria: str):
        super().__init__(f"La categoría {nombre_categoria} no está registrada.")
        self.nombre_categoria = nombre_categoria


class EquipoNoDisponible(ErrorDominio):
    """Se intenta prestar un equipo que no está DISPONIBLE (regla R2)."""

    def __init__(self, codigo_equipo: str, estado_actual: str):
        super().__init__(
            f"El equipo {codigo_equipo} no está disponible (estado: {estado_actual})."
        )
        self.codigo_equipo = codigo_equipo


class EquipoNoEncontrado(ErrorDominio):
    """No existe un equipo con el código indicado."""

    def __init__(self, codigo_equipo: str):
        super().__init__(f"No existe el equipo {codigo_equipo}.")
        self.codigo_equipo = codigo_equipo


class PrestamoNoEncontrado(ErrorDominio):
    """No existe un préstamo con el id indicado."""

    def __init__(self, prestamo_id: int):
        super().__init__(f"No existe el préstamo {prestamo_id}.")
        self.prestamo_id = prestamo_id


class LimitePrestamoExcedido(ErrorDominio):
    """Se lanza cuando se excede el límite de préstamos permitido - regla R1"""

    def __init__(self, mensaje="Se ha excedido el límite de préstamo permitido."):
        super().__init__(mensaje)
        self.mensaje = mensaje


class EstudianteConMultaActiva(ErrorDominio):
    """Se lanza cuando el estudiante tiene una multa activa - regla R4"""

    def __init__(self, mensaje="El estudiante tiene una multa activa y no puede realizar préstamos."):
        super().__init__(mensaje)
        self.mensaje = mensaje