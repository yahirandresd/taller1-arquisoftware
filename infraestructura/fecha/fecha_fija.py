from datetime import date
from aplicacion.puertos.proveedor_fecha import ProveedorFecha


class FechaFija(ProveedorFecha):
    #Siempre devuelve la misma fecha. Se usa en el modo demo

    def __init__(self, fecha: date):
        self._fecha = fecha

    def hoy(self) -> date:
        return self._fecha
