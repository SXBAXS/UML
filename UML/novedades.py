from productos import Productos

class Novedades(Productos):
    def __init__(self, clasificacion, tema, titulo, precio, autor, editorial, ano_edicion, preferencias):
        super().__init__(titulo, precio, autor, editorial, ano_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        self.clasificacion = nueva
