class Estudiantes:
    SIN_MULTA= 0

    def __init__(self, id: str, nombres: str, apellidos: str, correo: str, telefono: str, multa_pendiente: int = SIN_MULTA):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.telefono = telefono
        self.multa_pendiente = multa_pendiente

    def tiene_multa_pendiente(self) -> bool:
        #Con multa pendiente no puede pedir prestado - regla R4
        return self.multa_pendiente > self.SIN_MULTA

    def adicionar_multa(self, monto: int) -> None:
        self.multa_pendiente += monto