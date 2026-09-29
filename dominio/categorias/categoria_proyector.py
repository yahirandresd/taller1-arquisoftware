from dominio.categoria import Categoria


class CategoriaProyector(Categoria):
    NOMBRE = "PROYECTOR"
    DIAS_PLAZO = 2
    TARIFA_DIARIA = 6000

    def nombre(self) -> str:
        return self.NOMBRE

    def dias_plazo(self) -> int:
        return self.DIAS_PLAZO

    def tarifa_diaria(self) -> int:
        return self.TARIFA_DIARIA
