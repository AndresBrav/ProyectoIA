import sys

sys.path.append("c:/Users/ASUS/Desktop/PoyectoIA")  # Ajusta la ruta según tu entorno
from Rutas import *
from AgenteChofer import *
import tkinter as tk


class AgenteComprador:
    def __init__(self, nombre, mercadoObjetivo, dinero_Disponible, tiempo_De_Compra):
        """instanciamos las rutas que vamos usar"""
        # Rutas(nombre,tiempoRecorridoMinutos,distanciaMetros,pasaje)
        self.Ruta1 = Rutas("graficarRuta1", 34, 1700, 1.7)
        self.condutorRuta1 = AgenteChofer("Jose", "graficarRuta1")

        self.Ruta2LaPampa = Rutas("ruta2LaPampa", 58, 2900, 2.9)
        self.conductorRuta2LaPampa = AgenteChofer("Alex", "ruta2LaPampa")

        self.Ruta3SanAntonio = Rutas("ruta3SanAntonio", 20, 1000, 1)
        self.conductorRuta3SanAntonio = AgenteChofer("Alex", "ruta3SanAntonio")

        self.Ruta4 = Rutas("ruta4", 8, 400, 0.4)
        self.conductorRuta4 = AgenteChofer("Jurgen", "ruta4")

        self.Ruta4FidelAranibar = Rutas("ruta4FidelAranibar", 24, 1200, 1.2)
        self.conductorRuta4FidelAranibar = AgenteChofer("Paolo", "ruta4FidelAranibar")

        self.Ruta5SanAntonio = Rutas("ruta5SanAntonio", 80, 4000, 4)
        self.conductorRuta5SanAntonio = AgenteChofer("Paolo", "ruta5SanAntonio")

        self.Ruta5LaPampa = Rutas("ruta5LaPampa", 98, 4900, 4.9)
        self.conductorRuta5LaPampa = AgenteChofer("Paolo", "ruta5LaPampa")

        self.nombre = nombre
        self.mercadoObjetivo = mercadoObjetivo
        self.dinero_Disponible = dinero_Disponible
        self.tiempo_De_Compra = tiempo_De_Compra
        self.listaProductos = []

        self.casaObjetivo = "Casa"
        self.dineroGastado = 0
        self.tiempoUsado = 0
        self.viajeIda = False

    def ObtenerCasaObjetivo(self):
        return self.casaObjetivo

    def ObtenerDineroDisponible(self):
        return self.dinero_Disponible

    def ObtenerTiempoUsado(self):
        return self.tiempoUsado

    # aumentar el tiempo que vas usando
    def aumentarTiempo(self, incremento):
        self.tiempoUsado = self.tiempoUsado + incremento

    def obteneDineroGastado(self):
        return self.dineroGastado

    # aumentar el dinero que estas usando
    def aumentarGasto(self, incremento):
        self.dineroGastado = self.dineroGastado + incremento

    def obtenerMercadoObjetivo(self):
        return self.mercadoObjetivo

    def ObtenerTiempoDeCompraIngresado(self):
        return self.tiempo_De_Compra

    def DesplazamientoIda(self):
        nombreRuta1 = ""
        nombreRuta2 = ""
        if (
            (self.dinero_Disponible > 0)
            and (self.tiempoUsado < self.tiempo_De_Compra)
            and (self.tiempo_De_Compra > 31)
            and (
                self.Ruta1.get_tiempo_recorrido()
                + self.Ruta2LaPampa.get_tiempo_recorrido()
                < self.tiempo_De_Compra
            )
            and (
                self.Ruta5LaPampa.get_tiempo_recorrido()
                + self.Ruta4.get_tiempo_recorrido()
                < self.tiempo_De_Compra
            )
            and (
                self.Ruta4.get_tiempo_recorrido()
                + self.Ruta5SanAntonio.get_tiempo_recorrido()
                < self.tiempo_De_Compra
            )
            and (
                self.Ruta4FidelAranibar.get_tiempo_recorrido()
                + self.Ruta4.get_tiempo_recorrido()
                < self.tiempo_De_Compra
            )
            and (
                self.Ruta3SanAntonio.get_tiempo_recorrido()
                + self.Ruta1.get_tiempo_recorrido()
                < self.tiempo_De_Compra
            )
        ):
            if self.mercadoObjetivo == "La Pampa":
                if (self.Ruta1.get_pasaje() > self.Ruta4.get_pasaje()) or (
                    self.Ruta1.get_tiempo_recorrido()
                    > self.Ruta4.get_tiempo_recorrido()
                ):
                    """avanzar conductor"""
                    self.conductorRuta4.Avanzar()

                    nombreRuta1 = str(self.Ruta4.get_nombre())
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta4.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta4.get_pasaje())
                    self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta4.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())
                    # print("el dinero pagado al conductor es : "+str(self.conductorRuta4.get_cobrar()))

                else:
                    """avanzar conductor"""
                    self.condutorRuta1.Avanzar()
                    nombreRuta1 = str(self.Ruta1.get_nombre())
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta1.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta1.get_pasaje())
                    self.aumentarTiempo(self.Ruta1.get_tiempo_recorrido())
                    """ detener avance """
                    self.condutorRuta1.Detenerse()
                    """ pagar al condutor """
                    self.condutorRuta1.CobrarDinero(self.Ruta1.get_pasaje())

                if nombreRuta1 == "graficarRuta1":
                    nombreRuta2 = str(self.Ruta2LaPampa.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta2LaPampa.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta2LaPampa.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta2LaPampa.get_pasaje())
                    self.aumentarTiempo(self.Ruta2LaPampa.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta2LaPampa.Detenerse()
                    """ pagar al condutor """
                    self.conductorRuta2LaPampa.CobrarDinero(
                        self.Ruta2LaPampa.get_pasaje()
                    )

                else:
                    nombreRuta2 = str(self.Ruta5LaPampa.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta5LaPampa.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta5LaPampa.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta5LaPampa.get_pasaje())
                    self.aumentarTiempo(self.Ruta5LaPampa.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta5LaPampa.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta5LaPampa.CobrarDinero(
                        self.Ruta5LaPampa.get_pasaje()
                    )
            """ mercado objetivo San Antonio """
            if self.mercadoObjetivo == "San Antonio":
                if (self.Ruta1.get_pasaje() > self.Ruta4.get_pasaje()) or (
                    self.Ruta1.get_tiempo_recorrido()
                    > self.Ruta4.get_tiempo_recorrido()
                ):
                    nombreRuta1 = str(self.Ruta4.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta4.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta4.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta4.get_pasaje())
                    self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta4.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())
                else:
                    nombreRuta1 = str(self.Ruta1.get_nombre())
                    """avanzar conductor"""
                    self.condutorRuta1.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta1.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta1.get_pasaje())
                    self.aumentarTiempo(self.Ruta1.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta1.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta1.CobrarDinero(self.Ruta1.get_pasaje())

                if nombreRuta1 == "graficarRuta1":
                    nombreRuta2 = str(self.ruta3SanAntonio.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta3SanAntonio.Avanzar()

                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta3SanAntonio.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta3SanAntonio.get_pasaje())
                    self.aumentarTiempo(self.Ruta3SanAntonio.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta3SanAntonio.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta3SanAntonio.CobrarDinero(
                        self.Ruta3SanAntonio.get_pasaje()
                    )
                else:
                    nombreRuta2 = str(self.Ruta5SanAntonio.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta5SanAntonio.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta5SanAntonio.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta5SanAntonio.get_pasaje())
                    self.aumentarTiempo(self.Ruta5SanAntonio.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta5SanAntonio.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta5SanAntonio.CobrarDinero(
                        self.Ruta5SanAntonio.get_pasaje()
                    )

            if self.mercadoObjetivo == "Fidel Aranibar":
                nombreRuta1 = str(self.Ruta4.get_nombre())
                nombreRuta2 = str(self.Ruta4FidelAranibar.get_nombre())

                """ avanzar conductor """
                self.conductorRuta4.Avanzar()
                self.conductorRuta4FidelAranibar.Avanzar()

                self.dinero_Disponible = (
                    self.dinero_Disponible - self.Ruta4.get_pasaje()
                )
                self.dinero_Disponible = (
                    self.dinero_Disponible - self.Ruta4FidelAranibar.get_pasaje()
                )
                self.aumentarGasto(self.Ruta4.get_pasaje())
                self.aumentarGasto(self.Ruta4FidelAranibar.get_pasaje())
                self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                self.aumentarTiempo(self.Ruta4FidelAranibar.get_tiempo_recorrido())
                """ detener avance """
                self.conductorRuta4.Detenerse()
                self.conductorRuta4FidelAranibar.Detenerse()

                """ pagar al condutor """
                self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())
                self.conductorRuta4FidelAranibar.CobrarDinero(
                    self.Ruta4FidelAranibar.get_pasaje()
                )
                self.viajeIda = True
        else:
            detalles = tk.Tk()
            # Establecer la posición inicial de la ventana
            detalles.geometry("+1100+300")
            # Modificar el tamaño de la ventana
            detalles.geometry("400x300")
            # Mensajes
            mensaje1 = "No tienes dinero o tiempo  par realizar el viaje de Ida: "

            # Etiquetas con los mensajes
            label1 = tk.Label(detalles, text=mensaje1)
            label1.pack()

            # Iniciar el bucle de eventos
            detalles.mainloop()

        return nombreRuta1, nombreRuta2

    def DesplazamientoVuelta(self):
        nombreRuta1 = ""
        nombreRuta2 = ""
        if (
            (self.dinero_Disponible > 0)
            and (self.tiempoUsado < self.tiempo_De_Compra)
            and (self.viajeIda == True)
        ):
            if (self.mercadoObjetivo == "La Pampa") and (
                self.ObtenerCasaObjetivo() == "Casa"
            ):  # La Pampa
                if (
                    self.Ruta5LaPampa.get_pasaje() > self.Ruta2LaPampa.get_pasaje()
                ) or (
                    self.Ruta5LaPampa.get_tiempo_recorrido()
                    > self.Ruta2LaPampa.get_tiempo_recorrido()
                ):
                    """avanzar conductor"""
                    self.conductorRuta2LaPampa.Avanzar()

                    nombreRuta1 = str(self.Ruta2LaPampa.get_nombre())
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta2LaPampa.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta2LaPampa.get_pasaje())
                    self.aumentarTiempo(self.Ruta2LaPampa.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta2LaPampa.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta2LaPampa.CobrarDinero(
                        self.Ruta2LaPampa.get_pasaje()
                    )

                else:
                    """avanzar conductor"""
                    self.conductorRuta5LaPampa.Avanzar()
                    nombreRuta1 = str(self.Ruta5LaPampa.get_nombre())
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta5LaPampa.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta5LaPampa.get_pasaje())
                    self.aumentarTiempo(self.Ruta5LaPampa.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta5LaPampa.Detenerse()
                    """ pagar al condutor """
                    self.conductorRuta5LaPampa.CobrarDinero(
                        self.Ruta5LaPampa.get_pasaje()
                    )

                if nombreRuta1 == "ruta2LaPampa":
                    nombreRuta2 = str(self.Ruta1.get_nombre())
                    """avanzar conductor"""
                    self.condutorRuta1.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta1.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta1.get_pasaje())
                    self.aumentarTiempo(self.Ruta1.get_tiempo_recorrido())
                    """ detener avance """
                    self.condutorRuta1.Detenerse()
                    """ pagar al condutor """
                    self.condutorRuta1.CobrarDinero(self.Ruta2LaPampa.get_pasaje())

                else:
                    nombreRuta2 = str(self.Ruta4.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta4.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta4.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta4.get_pasaje())
                    self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta4.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())

            """ mercado  objetivo San Antonio  y casa """
            if (self.mercadoObjetivo == "San Antonio") and (
                self.ObtenerCasaObjetivo() == "Casa"
            ):
                if (
                    self.Ruta3SanAntonio.get_pasaje()
                    > self.Ruta5SanAntonio.get_pasaje()
                ) or (
                    self.Ruta3SanAntonio.get_tiempo_recorrido()
                    > self.Ruta5SanAntonio.get_tiempo_recorrido()
                ):
                    nombreRuta1 = str(self.Ruta5SanAntonio.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta5SanAntonio.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta5SanAntonio.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta5SanAntonio.get_pasaje())
                    self.aumentarTiempo(self.Ruta5SanAntonio.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta5SanAntonio.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta5SanAntonio.CobrarDinero(
                        self.Ruta5SanAntonio.get_pasaje()
                    )
                else:
                    nombreRuta1 = str(self.Ruta3SanAntonio.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta3SanAntonio.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta3SanAntonio.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta3SanAntonio.get_pasaje())
                    self.aumentarTiempo(self.Ruta3SanAntonio.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta3SanAntonio.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta3SanAntonio.CobrarDinero(
                        self.Ruta3SanAntonio.get_pasaje()
                    )

                if nombreRuta1 == "ruta5SanAntonio":
                    nombreRuta2 = str(self.Ruta4.get_nombre())
                    """avanzar conductor"""
                    self.conductorRuta4.Avanzar()

                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta4.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta4.get_pasaje())
                    self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                    """ detener avance """
                    self.conductorRuta4.Detenerse()

                    """ pagar al condutor """
                    self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())
                else:
                    nombreRuta2 = str(self.Ruta1.get_nombre())
                    """avanzar conductor"""
                    self.condutorRuta1.Avanzar()
                    self.dinero_Disponible = (
                        self.dinero_Disponible - self.Ruta1.get_pasaje()
                    )
                    self.aumentarGasto(self.Ruta1.get_pasaje())
                    self.aumentarTiempo(self.Ruta1.get_tiempo_recorrido())
                    """ detener avance """
                    self.condutorRuta1.Detenerse()

                    """ pagar al condutor """
                    self.condutorRuta1.CobrarDinero(self.Ruta1.get_pasaje())

            if (self.mercadoObjetivo == "Fidel Aranibar") and (
                self.ObtenerCasaObjetivo() == "Casa"
            ):
                nombreRuta1 = str(self.Ruta4FidelAranibar.get_nombre())
                nombreRuta2 = str(self.Ruta4.get_nombre())

                """ avanzar conductor """
                self.conductorRuta4FidelAranibar.Avanzar()
                self.conductorRuta4.Avanzar()

                self.dinero_Disponible = (
                    self.dinero_Disponible - self.Ruta4FidelAranibar.get_pasaje()
                )
                self.dinero_Disponible = (
                    self.dinero_Disponible - self.Ruta4.get_pasaje()
                )
                self.aumentarGasto(self.Ruta4FidelAranibar.get_pasaje())
                self.aumentarGasto(self.Ruta4.get_pasaje())
                self.aumentarTiempo(self.Ruta4FidelAranibar.get_tiempo_recorrido())
                self.aumentarTiempo(self.Ruta4.get_tiempo_recorrido())
                """ detener avance """
                self.conductorRuta4FidelAranibar.Detenerse()
                self.conductorRuta4.Detenerse()

                """ pagar al condutor """
                self.conductorRuta4FidelAranibar.CobrarDinero(
                    self.Ruta4FidelAranibar.get_pasaje()
                )
                self.conductorRuta4.CobrarDinero(self.Ruta4.get_pasaje())
        else:
            detalles = tk.Tk()
            # Establecer la posición inicial de la ventana
            detalles.geometry("+1100+300")
            # Modificar el tamaño de la ventana
            detalles.geometry("400x300")
            # Mensajes
            mensaje1 = "No tienes dinero o tiempo par realizar el viaje de Vuelta: "

            # Etiquetas con los mensajes
            label1 = tk.Label(detalles, text=mensaje1)
            label1.pack()

            # Iniciar el bucle de eventos
            detalles.mainloop()

        return nombreRuta1, nombreRuta2

    """ agregar una lista de productos a la lista """

    def agregar_Productos(self, Lista_de_producto_A_Comprar):
        self.listaProductos = Lista_de_producto_A_Comprar

    """ se obtiene la lista de productos que va comprar el agente """

    def obtener_Lista_ProductosA_Comprar(self):
        return self.listaProductos

    def ComprarProducto(self, precioProducto, productoAcomprar):
        tiempoIngresado = self.ObtenerTiempoDeCompraIngresado()
        tiempoUsado = self.ObtenerTiempoUsado()
        dineroGastado = self.obteneDineroGastado()
        dinero_Disponible = self.ObtenerDineroDisponible()

        if (
            (dinero_Disponible > 0)
            and (tiempoUsado < tiempoIngresado)
            and (dineroGastado < dinero_Disponible)
            and (precioProducto < dinero_Disponible)
            and (self.viajeIda == True)
        ):
            self.aumentarGasto(precioProducto)
            self.aumentarTiempo(0.5)  # aumenta el tiempo medio minuto por cada producto
            print("el dinero gastado es ", str(self.obteneDineroGastado()), " Bs")
            print("el tiempo gastado es : ", str(self.tiempoUsado), " Bs")

            detalles = tk.Tk()
            # Establecer la posición inicial de la ventana
            detalles.geometry("+1100+300")
            # Modificar el tamaño de la ventana
            detalles.geometry("400x300")
            # Mensajes
            mensaje1 = "Compraste Exitosamente el producto : " + productoAcomprar

            # Etiquetas con los mensajes
            label1 = tk.Label(detalles, text=mensaje1)
            label1.pack()

            # Iniciar el bucle de eventos
            detalles.mainloop()

        else:
            detalles = tk.Tk()
            # Establecer la posición inicial de la ventana
            detalles.geometry("+1100+300")
            # Modificar el tamaño de la ventana
            detalles.geometry("400x300")
            # Mensajes
            mensaje1 = (
                "No tienes dinero o tiempo para  comprar el producto : " + productoAcomprar
            )

            # Etiquetas con los mensajes
            label1 = tk.Label(detalles, text=mensaje1)
            label1.pack()

            # Iniciar el bucle de eventos
            detalles.mainloop()

    def __str__(self):
        return (
            f"AgenteComprador(nombre={self.nombre}, mercadoObjetivo={self.mercadoObjetivo}, "
            f"dinero_Disponible={self.dinero_Disponible}, tiempo_De_Compra={self.tiempo_De_Compra}, "
            f"listaProductos={self.listaProductos})"
        )
