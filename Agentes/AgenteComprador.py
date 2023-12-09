import sys

sys.path.append("c:/Users/ASUS/Desktop/PoyectoIA")  # Ajusta la ruta según tu entorno
from Rutas import *


class AgenteComprador:
    def __init__(self, nombre, mercadoObjetivo, dinero_Disponible, tiempo_De_Compra):
        """instanciamos las rutas que vamos usar"""
        # Rutas(nombre,tiempoRecorridoMinutos,distanciaMetros,pasaje)
        self.Ruta1 = Rutas("graficarRuta1", 34, 1700, 1.7)
        self.Ruta2LaPampa = Rutas("ruta2LaPampa", 58, 2900, 2.9)
        self.Ruta3SanAntonio = Rutas("ruta3SanAntonio", 20, 1000, 1)
        self.Ruta4 = Rutas("ruta4", 8, 400, 0.4)
        self.Ruta4FidelAranibar = Rutas("ruta4FidelAranibar", 24, 1200, 1.2)
        self.Ruta5SanAntonio = Rutas("ruta5SanAntonio", 80, 4000, 4)
        self.Ruta5LaPampa = Rutas("ruta5LaPampa", 98, 4900, 4.9)
        self.nombre = nombre
        self.mercadoObjetivo = mercadoObjetivo
        self.dinero_Disponible = dinero_Disponible
        self.tiempo_De_Compra = tiempo_De_Compra
        self.listaProductos = []

    def obtenerMercadoObjetivo(self):
        return self.mercadoObjetivo

    def DesplazamientoIda(self):
        nombreRuta1 = ""
        nombreRuta2 = ""

        if self.mercadoObjetivo == "La Pampa":
            if (self.Ruta1.get_pasaje() > self.Ruta4.get_pasaje()) or (
                self.Ruta1.get_tiempo_recorrido() > self.Ruta4.get_tiempo_recorrido()
            ):
                nombreRuta1 = str(self.Ruta4.get_nombre())
            else:
                nombreRuta1 = str(self.Ruta1.get_nombre())

            if nombreRuta1 == "graficarRuta1":
                nombreRuta2 = str(self.Ruta2LaPampa.get_nombre())
            else:
                nombreRuta2 = str(self.Ruta5LaPampa.get_nombre())

        if self.mercadoObjetivo == "San Antonio":
            if (self.Ruta1.get_pasaje() > self.Ruta4.get_pasaje()) or (
                self.Ruta1.get_tiempo_recorrido() > self.Ruta4.get_tiempo_recorrido()
            ):
                nombreRuta1 = str(self.Ruta4.get_nombre())
            else:
                nombreRuta1 = str(self.Ruta1.get_nombre())

            if nombreRuta1 == "graficarRuta1":
                nombreRuta2= str(self.ruta3SanAntonio.get_nombre())
            else:
                nombreRuta2=str(self.Ruta5SanAntonio.get_nombre())
        
        if self.mercadoObjetivo == "Fidel Aranibar":
            nombreRuta1 = str(self.Ruta4.get_nombre())
            nombreRuta2 = str(self.Ruta4FidelAranibar.get_nombre())

        return nombreRuta1, nombreRuta2

    """ se agrega un producto a la lista """

    def agregar_Productos(self, producto_A_Comprar):
        self.listaProductos.append(str(producto_A_Comprar))

    """ se obtiene la lista de productos que va comprar el agente """

    def obtener_Lista_Productos(self):
        return self.listaProductos

    def __str__(self):
        return (
            f"AgenteComprador(nombre={self.nombre}, mercadoObjetivo={self.mercadoObjetivo}, "
            f"dinero_Disponible={self.dinero_Disponible}, tiempo_De_Compra={self.tiempo_De_Compra}, "
            f"listaProductos={self.listaProductos})"
        )

