from dominio.categoria import Categoria
from dominio.excepciones import CategoriaNoRegistrada


class CatalogoCategorias:
    """Registro de categorías disponibles, buscadas por su nombre.

    Permite agregar categorías nuevas (como PROYECTOR) sin escribir
    cadenas de if/elif: solo se registran desde main.py.
    """

    def __init__(self):
        self._categorias = {}

    def registrar(self, categoria: Categoria) -> None:
        self._categorias[categoria.nombre()] = categoria

    def obtener(self, nombre: str) -> Categoria:
        if nombre not in self._categorias:
            raise CategoriaNoRegistrada(nombre)
        return self._categorias[nombre]
