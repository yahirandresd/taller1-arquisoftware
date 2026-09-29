from dominio.categoria import Categoria
from dominio.estado_entrega import EstadoEntrega
from dominio.estado_equipo import EstadoEquipo
from dominio.excepciones.equipo_no_disponible import EquipoNoDisponible


class Equipo:
    #Equipo de laboratorio que se presta a los estudiantes
    
    def __init__(self, codigo: str, categoria: Categoria,
                 estado: EstadoEquipo = EstadoEquipo.DISPONIBLE):
        self.codigo = codigo
        self.categoria = categoria
        self.estado = estado

    def esta_disponible(self) -> bool:
        return self.estado is EstadoEquipo.DISPONIBLE

    def marcar_prestado(self) -> None:
        
        #Solo se presta un equipo DISPONIBLE - regla R2
        if not self.esta_disponible():
            raise EquipoNoDisponible(self.codigo, self.estado.value)
        self.estado = EstadoEquipo.PRESTADO

    def recibir(self, condicion: EstadoEntrega) -> None:
        #Co daño pasa a EN_MANTENIMIENTO; sin daño queda en DISPONIBLE - regla R6
        self.estado = condicion.estado_final()
