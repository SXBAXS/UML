from libro import Libro
from revista import Revista
from segunda_mano import ArticuloSegundaMano
from articulo_online import ArticuloOnline
from novedades import Novedades
from usuario import Usuario
from Servidor import Servidor
from procesador import Procesador
from indexador import Indexador
from recolector import Recolector
from hilo import Hilo
from editorial import Editorial
from productos import Productos

libro = Libro(
    genero="Novela",
    titulo="Cien Años de Soledad",
    precio=50000,
    autor="Gabriel García Márquez",
    editorial="Sudamericana",
    ano_edicion=1967,
    preferencias=["Literatura", "Clásico"]
)

revista = Revista(
    categoria="Ciencia",
    titulo="National Geographic",
    precio=20000,
    autor="Varios",
    editorial="NatGeo",
    ano_edicion=2024,
    preferencias=["Naturaleza"]
)

articulo_usado = ArticuloSegundaMano(
    clasificacion="Usado",
    tema="Tecnología",
    vendedor="Juan",
    titulo="Libro Python",
    precio=30000,
    autor="Autor X",
    editorial="TechBooks",
    ano_edicion=2020,
    preferencias=["Programación"]
)

articulo_online = ArticuloOnline(
    tema="Programación",
    titulo="Curso Python",
    precio=0,
    autor="Admin",
    editorial="Online",
    ano_edicion=2025,
    preferencias=["Educación"]
)

novedad = Novedades(
    clasificacion="Nuevo",
    tema="Libros",
    titulo="IA Moderna",
    precio=60000,
    autor="Autor IA",
    editorial="TechPress",
    ano_edicion=2025,
    preferencias=["Tecnología"]
)

usuario = Usuario(
    nombre="Sebastian",
    apellido="Gomez",
    cuenta="12345",
    direccion="Calle 1",
    login="seb",
    password="1234"
)

servidor = Servidor()
procesador = Procesador()
indexador = Indexador()
recolector = Recolector()
hilo = Hilo()
editorial = Editorial("Planeta", "Calle 10", "5551234")


print(libro.ver_catalogo())
print(usuario.comprar(libro))
print(usuario.vender(revista))
print(articulo_online.publicar())
print(servidor.muestra_pagina())
print(procesador.realizar_pago())
