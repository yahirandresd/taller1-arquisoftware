from dominio.excepciones.error_dominio import ErrorDominio

class CategoriaNoRegistrada(ErrorDominio):
    """Se pide una categoría que no fue registrada en el catálogo."""

    def __init__(self, nombre_categoria: str):
        super().__init__(f"La categoría {nombre_categoria} no está registrada.")
        self.nombre_categoria = nombre_categoria
