from enum import Enum

from dominio.estado_equipo import EstadoEquipo


class EstadoEntrega(Enum):
    #la condición en la que el estudiante entrega el equipo - regla R6

    SIN_DANO = "SIN_DANO"
    CON_DANO = "CON_DANO"

    def estado_final(self) -> EstadoEquipo:
        #Estado en el que queda el equipo después de la etregra
        
        if self is EstadoEntrega.CON_DANO:
            return EstadoEquipo.EN_MANTENIMIENTO
        return EstadoEquipo.DISPONIBLE
