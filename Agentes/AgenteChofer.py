class AgenteChofer:
    def __init__(self, nombre, nombreRuta):
        self.nombre = nombre
        self.nombreRuta = nombreRuta
        self.avance = False
        self.cobrarDinero = 0

    def Avanzar(self):
        avance = True

    def Detenerse(self):
        avance = False

    # Getter para el atributo nombre
    def get_nombre(self):
        return self.nombre

    # Setter para el atributo nombre
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # Getter para el atributo nombreRuta
    def get_nombreRuta(self):
        return self.nombreRuta

    # Setter para el atributo nombreRuta
    def set_nombreRuta(self, nueva_ruta):
        self.nombreRuta = nueva_ruta

    # Getter para el atributo cobrar
    def get_cobrar(self):
        return self.cobrarDinero


    def CobrarDinero(self, nuevo_cobrar):
        self.cobrarDinero = self.cobrarDinero + nuevo_cobrar

