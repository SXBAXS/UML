from productos import Productos

class Libro(Productos):
    def __init__(self, genero, titulo, precio, autor, editorial, ano_edicion, preferencias):
        super().__init__(titulo, precio, autor, editorial, ano_edicion, preferencias)
        self.genero = genero

    def mostrar_informacion(self):
        info = (
            f"Género: {self.genero}\n"
            f"Título: {self.titulo}\n"
            f"Precio: ${self.precio}\n"
            f"Autor: {self.autor}\n"
            f"Editorial: {self.editorial}\n"
            f"Año de Edición: {self.ano_edicion}\n"
            f"Preferencias: {', '.join(self.preferencias)}"
        )
        return info