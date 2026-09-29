from enum import Enum

class EstadoEquipo(Enum):
    
    DISPONIBLE = "DISPONIBLE"
    PRESTADO = "PRESTADO"
    EN_MANTENIMIENTO = "EN_MANTENIMIENTO"