class Rutas:
    def __init__(self, nombre, tiempo_recorrido, distancia_metros, pasaje):
        self.nombre = nombre
        self.tiempo_recorrido = tiempo_recorrido
        self.distancia_metros = distancia_metros
        self.pasaje = pasaje

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_tiempo_recorrido(self):
        return self.tiempo_recorrido

    def set_tiempo_recorrido(self, nuevo_tiempo_recorrido):
        self.tiempo_recorrido = nuevo_tiempo_recorrido

    def get_distancia_metros(self):
        return self.distancia_metros

    def set_distancia_metros(self, nueva_distancia_metros):
        self.distancia_metros = nueva_distancia_metros

    def get_pasaje(self):
        return self.pasaje

    def set_pasaje(self, nuevo_pasaje):
        self.pasaje = nuevo_pasaje

# from Rutas import *
# Crear una instancia de la clase Rutas
# ruta_1 = Rutas("Ruta A", 30, 5000, 2.5)
# # Utilizar setters para actualizar algunos valores
# ruta_1.set_tiempo_recorrido(40)
# ruta_1.set_pasaje(3.0)
# print(ruta_1.get_distancia_metros(),ruta_1.get_pasaje())

