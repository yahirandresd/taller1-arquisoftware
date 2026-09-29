from dominio.excepciones.error_dominio import ErrorDominio

class EquipoNoEncontrado(ErrorDominio):
    """No existe un equipo con el código indicado."""

    def __init__(self, codigo_equipo: str):
        super().__init__(f"No existe el equipo {codigo_equipo}.")
        self.codigo_equipo = codigo_equipo
