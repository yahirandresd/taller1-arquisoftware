from dominio.categoria import Categoria


class CategoriaPortatil(Categoria):
    NOMBRE = "PORTATIL"
    DIAS_PLAZO = 3
    TARIFA_DIARIA = 5000

    def nombre(self) -> str:
        return self.NOMBRE

    def dias_plazo(self) -> int:
        return self.DIAS_PLAZO

    def tarifa_diaria(self) -> int:
        return self.TARIFA_DIARIA
