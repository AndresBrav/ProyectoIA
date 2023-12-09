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

    def __str__(self):
        return f"Ruta: {self.nombre}\nTiempo Recorrido: {self.tiempo_recorrido} horas\n" \
               f"Distancia: {self.distancia_metros} metros\nPasaje: {self.pasaje}"



