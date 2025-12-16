class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        return "Sugerencia enviada"

    def leer(self):
        return "Leyendo"

    def comprar(self, producto):
        return producto.comprar()

    def vender(self, producto):
        return producto.vender()

    def realizar_reclamacion(self):
        return "Reclamación realizada"
