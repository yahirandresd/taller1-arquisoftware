class LimitePrestamoExcedido(Exception):
    """Excepción lanzada cuando se excede el límite de préstamo permitido."""
    def __init__(self, mensaje="Se ha excedido el límite de préstamo permitido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EquipoNoDisponible(Exception):
    """Se lanza cuando el equipo no está en estado DISPONIBLE (R2)."""
    def __init__(self, mensaje="El equipo no esta disponible para prestamo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EstudianteConMultaActiva(Exception):
    """Se lanza cuando el estudiante tiene una multa activa (R3)."""
    def __init__(self, mensaje="El estudiante tiene una multa activa y no puede realizar préstamos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)