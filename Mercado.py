from Productos import *


class Mercado:
    def __init__(self, nombre, listaproductos):
        self.nombre = nombre
        self.listaproductos = listaproductos

    # Getter para obtener el nombre del mercado
    def obtener_nombre(self):
        return self.nombre

    # Setter para cambiar el nombre del mercado
    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # Getter para obtener lista de productos
    def obtener_Lista_Productos(self):
        return self.listaproductos

    def __str__(self):
        return f"Mercado(nombre={self.nombre}, lista_productos={self.lista_productos})"


