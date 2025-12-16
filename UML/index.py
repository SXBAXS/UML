from libro import libro
from revista import revista
from productos import productos
from novedades import novedades
from segunda_mano import segunda_mano

# Crear instancias de cada clase para demostrar su funcionalidad
libro1 = libro("Cien Años de Soledad", 20.0, "Gabriel García Márquez", "Editorial Sudamericana", 1967, ["Realismo Mágico"], "Novela", 417)
revista1 = revista("National Geographic", 5.0, "Varios", "National Geographic Partners", 2024, ["Ciencia", "Naturaleza"], 150, "Ciencia")
segunda_mano1 = segunda_mano("El Principito", 10.0, "Antoine de Saint-Exupéry", "Literatura Infantil", "Fantasía", "Juan Pérez", "Bueno")
novedad1 = novedades("La Sombra del Viento", 25.0, "Carlos Ruiz Zafón", "Editorial Planeta", 2001, ["Misterio", "Suspenso"], "Adulto", "Novela Negra")
articulo1 = productos("Artículo Genérico", 15.0, "Autor Desconocido", "Editorial X", 2020, ["General"])

# Mostrar información de cada producto
print(libro1.mostrar_informacion())
print(revista1.mostrar_informacion())
print(segunda_mano1.mostrar_informacion())
print(novedad1.mostrar_informacion())
print(articulo1.mostrar_informacion())

# Cambiar clasificación de la novedad y mostrar la nueva clasificación
print(novedad1.cambiar_clasificacion("Juvenil"))
# Vender y comprar productos
print(libro1.vender())
print(revista1.comprar())
print(segunda_mano1.vender())
print(novedad1.comprar())
print(articulo1.vender())
print(articulo1.comprar())


