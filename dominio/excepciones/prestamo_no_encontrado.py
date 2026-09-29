from dominio.excepciones.error_dominio import ErrorDominio


class PrestamoNoEncontrado(ErrorDominio):
    """No existe un préstamo con el id indicado."""

    def __init__(self, prestamo_id: int):
        super().__init__(f"No existe el préstamo {prestamo_id}.")
        self.prestamo_id = prestamo_id
