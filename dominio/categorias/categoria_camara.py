from dominio.categoria import Categoria


class CategoriaCamara(Categoria):
    NOMBRE = "CAMARA"
    DIAS_PLAZO = 2
    TARIFA_DIARIA = 8000

    def nombre(self) -> str:
        return self.NOMBRE

    def dias_plazo(self) -> int:
        return self.DIAS_PLAZO

    def tarifa_diaria(self) -> int:
        return self.TARIFA_DIARIA
