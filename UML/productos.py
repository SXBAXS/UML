class Productos:
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, preferencias):
        self.titulo = titulo
        self.precio = precio
        self.autor = autor
        self.editorial = editorial
        self.ano_edicion = ano_edicion
        self.preferencias = preferencias  # lista

    def vender(self):
        return f"El producto '{self.titulo}' ha sido vendido por {self.precio}."

    def comprar(self):
        return f"El producto '{self.titulo}' ha sido comprado por {self.precio}."

    def ver_catalogo(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Editorial: {self.editorial}\n"
            f"Año de Edición: {self.ano_edicion}\n"
            f"Precio: {self.precio}"
        )
