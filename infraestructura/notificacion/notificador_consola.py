from aplicacion.puertos.notificador import Notificador
from dominio.prestamo import Prestamo


class NotificadorConsola(Notificador):
    #Simula las notificaciones en la consola

    def notificar_fecha_limite(self, estudiante_id: str, prestamo: Prestamo) -> None:
        print(f"[NOTIFICACIÓN] {estudiante_id}: prestaste {prestamo.codigo_equipo}. "
              f"Debes devolverlo a más tardar el {prestamo.fecha_limite}.")

    def notificar_multa(self, estudiante_id: str, prestamo: Prestamo) -> None:
        print(f"[NOTIFICACIÓN] {estudiante_id}: devolviste {prestamo.codigo_equipo} "
              f"con retraso. Multa: {self._formatear_pesos(prestamo.multa)}.")

    def _formatear_pesos(self, monto: int) -> str:
        """Convierte 24000 en "$24.000"."""
        return "$" + f"{monto:,}".replace(",", ".")
