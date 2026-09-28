from datetime import date
from aplicacion.puertos.proveedor_fecha import ProveedorFecha

class FechaSistema(ProveedorFecha):
    def hoy(self) -> date:
        return date.today()
    