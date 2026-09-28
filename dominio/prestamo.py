from datetime import datetime

class Prestamo:
    def  __init__(self, id: str, estudiante_id: str, codigo_equipo: str, fecha_inicio: datetime, fecha_limite: datetime, estado: str = "ACTIVO", multa: int = 0):
        self.id = id
        self.estudiante_id = estudiante_id
        self.codigo_equipo = codigo_equipo
        self.fecha_inicio = fecha_inicio
        self.fecha_limite= fecha_limite
        self.estado = estado
        self.multa = multa

    def calcular_multa(self, fecha_entrega: datetime, tarifa_diaria : int) -> int:
        """Calcula la multa basada en la fecha de entrega y la tarifa diaria."""
        self.fecha_devolucion = fecha_entrega
        self.estado = "DEVUELTO"
        if self.fecha_devolucion <= self.fecha_limite:
            return 0
        dias_retraso = (self.fecha_devolucion - self.fecha_limite).days
        self.multa = dias_retraso * tarifa_diaria
        return self.multa