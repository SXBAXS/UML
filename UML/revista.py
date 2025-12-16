from productos import Productos

class Revista(Productos):
    def __init__(self, categoria, titulo, precio, autor, editorial, ano_edicion, preferencias):
        super().__init__(titulo, precio, autor, editorial, ano_edicion, preferencias)
        self.categoria = categoria
        
    
