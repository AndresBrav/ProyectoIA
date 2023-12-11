import sys

sys.path.append("c:/Users/ASUS/Desktop/PoyectoIA/Agentes")
from Agentes.AgenteComprador import *
from Agentes.AgenteChofer import *
from GraficarCamino import cargarGrafico
from GraficarCaminoVuelta import cargarGraficoVuelta
from Agentes.AgenteVendedor import *
from Rutas import *
from Productos import *
from Mercado import *

# from Agentes.AgenteComprador import *
import tkinter as tk
from tkinter import simpledialog


""" el usuario introduce cuánto dinero tendrá
el agente para el transporte(Tanto de ida, y vuelta), que productos debe comprar. Y
también el usuario introduce el tiempo que debe tardar en su compra. """
dinero_Disponible = 0
listaProductos = []
tiempo_De_Compra = 0
Mercado_Objetivo = ""


# Función para ingresar datos
def ingresar_datos():
    try:
        global dinero_Disponible
        dinero_Disponible = simpledialog.askfloat(
            "Ingreso de datos", "Por favor, ingresa el dinero disponible para el viaje"
        )

        # Crear una lista para almacenar las cantidades de productos
        global listaProductos
        listaProductos = []

        # Solicitar al usuario que ingrese la cantidad de productos
        contador = 0
        # while True:
        while contador < 4:
            producto = simpledialog.askstring(
                "Ingreso de datos",
                "Por favor, ingresa el producto (o introduce la palabra (stop) para terminar):",
            )

            # Si el producto  es stop, salir del bucle
            if producto == "stop":
                break
            # Agregar el producto a   la lista
            listaProductos.append(str(producto))
            contador = contador + 1

        global tiempo_De_Compra
        tiempo_De_Compra = simpledialog.askfloat(
            "Ingreso de datos",
            "Por favor, ingresa el tiempo que va tardar toda la compra:",
        )

        global Mercado_Objetivo
        Mercado_Objetivo = simpledialog.askstring(
            "Ingreso de datos",
            "Por favor, ingresa el Mercado donde vas a realizar la compra (Fidel Aranibar,La Pampa,San Antonio)",
        )

    except (ValueError, TypeError):
        print("Error: Ingresa un valor numérico válido.")


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Ingreso de Datos")
# Modificar el tamaño de la ventana
ventana.geometry("400x300")
# Cambiar el color de fondo de la ventana
ventana.configure(bg="#FFFFFF")

# Crear un botón que llame a la función al hacer clic
boton_ingresar = tk.Button(
    ventana,
    text="Ingresar Datos",
    command=ingresar_datos,
    font=("Arial", 14),
    bg="#FFFFFF",  # Cambiar el color de fondo del botón
    fg="black",  # Cambiar el color del texto del botón
    padx=20,  # Añadir relleno horizontal
    pady=10,  # Añadir relleno vertical)
)
boton_ingresar.pack(pady=20)
# Ejemplo de uso
ventana.mainloop()

# Instanciamos el agente que va realizar la compra
agentecompra = AgenteComprador(
    "Andres", Mercado_Objetivo, dinero_Disponible, tiempo_De_Compra
)
agentecompra.agregar_Productos(listaProductos)
primerRuta, segundaRuta = agentecompra.DesplazamientoIda()


""" instanciamos los Agentes de Venta """
agenteVendedorLaPampa = AgenteVendedor("Juan", "La Pampa")
agenteVendedorSanAntonio = AgenteVendedor("Paolo", "San Antonio")
agenteVendedorFidelAranibar = AgenteVendedor("Kevin", "Fidel Aranibar")


if "La Pampa" == agentecompra.obtenerMercadoObjetivo():
    """realizamos la compra en La Pampa"""
    contador = 0
    tamañoDeLista = len(agentecompra.obtener_Lista_ProductosA_Comprar())
    # print("el tamaño de lista es : ",str(tamañoDeLista))
    while contador < tamañoDeLista:
        mercadoComprador = (
            agentecompra.obtenerMercadoObjetivo()
        )  # mercado donde se realizara la compra
        mercadoVendedor = agenteVendedorLaPampa.get_Mercado_Que_Atiende()
        if mercadoComprador == mercadoVendedor:
            productoAcomprar = agentecompra.obtener_Lista_ProductosA_Comprar()[
                contador
            ]  # muestra un producto de la lista
            precioProducto = 0

            """ Verificar que el producto esta en la lista  del Mercado"""
            contador1 = 0
            while contador1 < len(agenteVendedorLaPampa.get_lista_la_pampa()):
                if (
                    productoAcomprar
                    == agenteVendedorLaPampa.get_lista_la_pampa()[
                        contador1
                    ].get_nombre()
                ):
                    precioProducto = agenteVendedorLaPampa.get_lista_la_pampa()[
                        contador1
                    ].get_precio_unitario()  # precio
                    """ comprar el producto """
                    agenteVendedorLaPampa.AtenderCliente()
                    agentecompra.ComprarProducto(precioProducto, productoAcomprar)
                    agenteVendedorLaPampa.aumentarDineroRecaudado(precioProducto)
                    agenteVendedorLaPampa.DejarAtenderCliente()

                contador1 = contador1 + 1

            print("el precio del producto es ", precioProducto)
            print("la producto a comprar es : ", productoAcomprar)
        contador = contador + 1

if "San Antonio" == agentecompra.obtenerMercadoObjetivo():
    """realizamos la compra en San Antonio"""
    contador = 0
    tamañoDeLista = len(agentecompra.obtener_Lista_ProductosA_Comprar())
    # print("el tamaño de lista es : ",str(tamañoDeLista))
    while contador < tamañoDeLista:
        mercadoComprador = (
            agentecompra.obtenerMercadoObjetivo()
        )  # mercado donde se realizara la compra
        mercadoVendedor = agenteVendedorSanAntonio.get_Mercado_Que_Atiende()
        if mercadoComprador == mercadoVendedor:
            productoAcomprar = agentecompra.obtener_Lista_ProductosA_Comprar()[
                contador
            ]  # muestra un producto de la lista
            precioProducto = 0

            """ Verificar que el producto esta en la lista  del Mercado"""
            contador1 = 0
            while contador1 < len(agenteVendedorSanAntonio.get_lista_san_antonio()):
                if (
                    productoAcomprar
                    == agenteVendedorSanAntonio.get_lista_san_antonio()[
                        contador1
                    ].get_nombre()
                ):
                    precioProducto = agenteVendedorSanAntonio.get_lista_san_antonio()[
                        contador1
                    ].get_precio_unitario()  # precio
                    """ comprar el producto """
                    agenteVendedorSanAntonio.AtenderCliente()
                    agentecompra.ComprarProducto(precioProducto, productoAcomprar)
                    agenteVendedorSanAntonio.aumentarDineroRecaudado(precioProducto)
                    agenteVendedorSanAntonio.DejarAtenderCliente()

                contador1 = contador1 + 1

            print("el precio del producto es ", precioProducto)
            print("el producto a comprar es : ", productoAcomprar)
            print("\n")
        contador = contador + 1

if "Fidel Aranibar" == agentecompra.obtenerMercadoObjetivo():
    """realizamos la compra en Fidel Aranibar"""
    contador = 0
    tamañoDeLista = len(agentecompra.obtener_Lista_ProductosA_Comprar())
    # print("el tamaño de lista es : ",str(tamañoDeLista))
    while contador < tamañoDeLista:
        mercadoComprador = (
            agentecompra.obtenerMercadoObjetivo()
        )  # mercado donde se realizara la compra
        mercadoVendedor = agenteVendedorFidelAranibar.get_Mercado_Que_Atiende()
        if mercadoComprador == mercadoVendedor:
            productoAcomprar = agentecompra.obtener_Lista_ProductosA_Comprar()[
                contador
            ]  # muestra un producto de la lista
            precioProducto = 0

            """ Verificar que el producto esta en la lista  del Mercado"""
            contador1 = 0
            while contador1 < len(
                agenteVendedorFidelAranibar.get_lista_fidel_Aranibar()
            ):
                if (
                    productoAcomprar
                    == agenteVendedorFidelAranibar.get_lista_fidel_Aranibar()[
                        contador1
                    ].get_nombre()
                ):
                    precioProducto = (
                        agenteVendedorFidelAranibar.get_lista_fidel_Aranibar()[
                            contador1
                        ].get_precio_unitario()
                    )  # precio
                    """ comprar el producto """
                    agenteVendedorFidelAranibar.AtenderCliente()
                    agentecompra.ComprarProducto(precioProducto, productoAcomprar)
                    agenteVendedorFidelAranibar.aumentarDineroRecaudado(precioProducto)
                    agenteVendedorFidelAranibar.DejarAtenderCliente()

                contador1 = contador1 + 1

            print("el precio del producto es ", precioProducto)
            print("la producto a comprar es : ", productoAcomprar)
        contador = contador + 1

# primerRutaVuelta, segundaRutaVuelta = agentecompra.DesplazamientoVuelta()

dineroGastado = agentecompra.obteneDineroGastado()
tiempoUsado = agentecompra.ObtenerTiempoUsado()

# Crear la ventana principal de los detalles de compra que se va hacer
detalles = tk.Tk()
# Establecer la posición inicial de la ventana
detalles.geometry("+1100+300")
# Modificar el tamaño de la ventana
detalles.geometry("400x300")
# Mensajes
mensaje1 = "el dinero disponible es : " + str(dinero_Disponible) + " Bs"
mensaje2 = f"Los productos que se quiere comprar son : {listaProductos}"
mensaje3 = "el tiempo disponible en minutos  es : " + str(tiempo_De_Compra)
mensaje4 = "El mercado objetivo es : " + str(Mercado_Objetivo)

mensaje5 = "El dinero gastado es " + str(agentecompra.obteneDineroGastado()) + " Bs"
mensaje7 = "El tiempo usado es  : " + str(agentecompra.ObtenerTiempoUsado()) + " minutos"

# Etiquetas con los mensajes
label1 = tk.Label(detalles, text=mensaje1)
label1.pack()

label2 = tk.Label(detalles, text=mensaje2)
label2.pack()

label3 = tk.Label(detalles, text=mensaje3)
label3.pack()

label4 = tk.Label(detalles, text=mensaje4)
label4.pack()


label6 = tk.Label(detalles, text="")
label6.pack()

label5 = tk.Label(detalles, text=mensaje5)
label5.pack()

label7 = tk.Label(detalles, text=mensaje7)
label7.pack()

# Iniciar el bucle de eventos
detalles.mainloop()

cargarGrafico(primerRuta,segundaRuta)

# cargarGraficoVuelta(primerRutaVuelta, segundaRutaVuelta)
