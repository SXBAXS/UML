from productos import Productos

class ArticuloSegundaMano(Productos):
    def __init__(self, clasificacion, tema, vendedor, titulo, precio, autor, editorial, ano_edicion, preferencias):
        super().__init__(titulo, precio, autor, editorial, ano_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor
