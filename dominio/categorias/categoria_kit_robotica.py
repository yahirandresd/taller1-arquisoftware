from dominio.categoria import Categoria


class CategoriaKitRobotica(Categoria):
    NOMBRE = "KIT_ROBOTICA"
    DIAS_PLAZO = 1
    TARIFA_DIARIA = 12000

    def nombre(self) -> str:
        return self.NOMBRE

    def dias_plazo(self) -> int:
        return self.DIAS_PLAZO

    def tarifa_diaria(self) -> int:
        return self.TARIFA_DIARIA
