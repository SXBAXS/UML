from productos import Productos

class ArticuloOnline(Productos):
    def __init__(self, tema, titulo, precio, autor, editorial, ano_edicion, preferencias):
        super().__init__(titulo, precio, autor, editorial, ano_edicion, preferencias)
        self.tema = tema

    def publicar(self):
        return f"Artículo {self.titulo} publicado"

    def descargar(self):
        return f"Artículo {self.titulo} descargado"
    
    def ver_detalles(self):
        detalles_base = super().ver_catalogo()
        return f"{detalles_base}\nTema: {self.tema}"
    
    