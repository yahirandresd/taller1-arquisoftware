from enum import Enum

class EstadoEquipo(Enum):
    
    DISPONIBLE = "DISPONIBLE"
    PRESTADO = "PRESTADO"
    EN_MANETENIMIENTO = "EN_MANTENIMIENTO"