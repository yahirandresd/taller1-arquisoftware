from datetime import date
from dominio.estado_prestamo import EstadoPrestamo

class Prestamo:
    #Préstamo de un equipo a un estudiante

    def __init__(self, id: int | None, estudiante_id: str, codigo_equipo: str, fecha_inicio: date, fecha_limite: date, 
                 fecha_devolucion: date | None = None, estado: EstadoPrestamo = EstadoPrestamo.ACTIVO, multa: int = 0):
        self.id = id
        self.estudiante_id = estudiante_id
        self.codigo_equipo = codigo_equipo
        self.fecha_inicio = fecha_inicio
        self.fecha_limite = fecha_limite
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
        self.multa = multa

    def cerrar(self, fecha_devolucion: date, multa: int) -> None:
        #Registra la devolución; la multa la calcula CalculadoraMulta - regla R5
        self.fecha_devolucion = fecha_devolucion
        self.multa = multa
        self.estado = EstadoPrestamo.DEVUELTO
