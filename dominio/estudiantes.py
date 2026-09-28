class Estudiantes:
    def __init__(self, id : str, nombres : str, apellidos : str, correo : str, telefono: str, prest_activos: int, multa_pend: bool):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.telefono = telefono
        self.prest_activos = prest_activos
        self.multa_pend = multa_pend

    def tiene_multa_activa(self) -> bool:
        """Verifica si el estudiante tiene una multa activa."""
        return self.multa_pend

    def adicionar_multa(self) -> None:
        """Marca al estudiante como con multa activa."""
        self.multa_pend = True