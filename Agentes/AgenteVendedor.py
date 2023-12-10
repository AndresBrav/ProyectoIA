import sys

sys.path.append("c:/Users/ASUS/Desktop/PoyectoIA")  # Ajusta la ruta según tu entorno
from Rutas import *
from Productos import *
from Mercado import *


class AgenteVendedor:
    def __init__(self, nombre_vendedor, mercadoQueAtiende):
        self.nombre_vendedor = nombre_vendedor
        self.dinero_recaudado = 0
        self.atender = False
        self.mercadoQueAtiende = mercadoQueAtiende

        """ instanciamos los mercados """
        self.listaLaPampa = []
        self.Arroz = Productos("arroz", 23, 280)
        self.Huevo = Productos("huevo", 23, 60)
        self.Papa = Productos("papa", 23, 28)
        self.Carne = Productos("carne", 23, 35)

        self.listaLaPampa = [self.Arroz, self.Huevo, self.Papa, self.Carne]

        self.listaSanAntonio = []
        self.Cuaderno = Productos("cuaderno", 100, 12)
        self.Guitarra = Productos("guitarra", 20, 420)
        self.Hilos = Productos("hilos", 100, 2)
        self.Zapatos = Productos("zapatos", 50, 150)

        self.listaSanAntonio = [self.Cuaderno, self.Guitarra, self.Hilos, self.Zapatos]

        self.listaFidelAranibar = []
        self.Saco = Productos("saco", 100, 350)
        self.Corbata = Productos("corbata", 20, 25)
        self.Juguete = Productos("juguete", 100, 90)
        self.Torta = Productos("torta", 50, 30)

        self.listaFidelAranibar = [self.Saco, self.Corbata, self.Juguete, self.Torta]

    def aumentarDineroRecaudado(self, incremento):
        self.dinero_recaudado = self.dinero_recaudado + incremento

    def obtenerDineroRecaudado(self):
        return self.dinero_recaudado

    def get_Mercado_Que_Atiende(self):
        return self.mercadoQueAtiende

    def AtenderCliente(self):
        self.atender = True

    def getAtenderCliente(self):
        return self.atender

    def DejarAtenderCliente(self):
        self.atender = False

    # def venderProducto(self, producto):

    # def cobrar(self, monto_cobro):
    #     print()

    # Getter y setter para listaLaPampa
    def get_lista_la_pampa(self):
        return self.listaLaPampa

    def get_lista_san_antonio(self):
        return self.listaSanAntonio

    def get_lista_fidel_Aranibar(self):
        return self.listaFidelAranibar


# agente1 = AgenteVendedor("juan", 15)
# print(agente1.get_lista_la_pampa()[0].get_nombre())
