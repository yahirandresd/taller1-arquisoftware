from datetime import date
from dominio.categoria import Categoria

class CalculadoraMulta:
    #Calcula la multa por retraso en la devolución - regla R5

    SIN_MULTA = 0

    def calcular(self, fecha_limite: date, fecha_entrega: date, categoria: Categoria) -> int:

        dias_de_retraso = (fecha_entrega - fecha_limite).days
        if dias_de_retraso <= 0:
            return self.SIN_MULTA
        return dias_de_retraso * categoria.tarifa_diaria()
