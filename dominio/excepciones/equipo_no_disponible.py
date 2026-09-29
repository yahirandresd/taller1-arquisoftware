from dominio.excepciones.error_dominio import ErrorDominio

class EquipoNoDisponible(ErrorDominio):
    """Se intenta prestar un equipo que no está DISPONIBLE (regla R2)."""

    def __init__(self, codigo_equipo: str, estado_actual: str):
        super().__init__(
            f"El equipo {codigo_equipo} no está disponible (estado: {estado_actual})."
        )
        self.codigo_equipo = codigo_equipo
