from GraficarCamino import *
from Rutas import *
from Productos import *
from Mercado import *
from Agentes.AgenteComprador import *
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
        while True:
            producto = simpledialog.askstring(
                "Ingreso de datos",
                "Por favor, ingresa el producto (o introduce la palabra (stop) para terminar):",
            )

            # Si el producto  es stop, salir del bucle
            if producto == "stop":
                break
            # Agregar el producto a   la lista
            listaProductos.append(str(producto))

        global tiempo_De_Compra
        tiempo_De_Compra = simpledialog.askfloat(
            "Ingreso de datos",
            "Por favor, ingresa el tiempo que va tardar toda la compra:",
        )

        global Mercado_Objetivo
        Mercado_Objetivo = simpledialog.askstring(
            "Ingreso de datos",
            "Por favor, ingresa el Mercado donde vas a realizar la compra",
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

print("el mercado objetivo es " + Mercado_Objetivo)

agentecompra = AgenteComprador(
    "Andres", Mercado_Objetivo, dinero_Disponible, tiempo_De_Compra
)
agentecompra.agregar_Productos(listaProductos)

primerRuta,segundaRuta=agentecompra.DesplazamientoIda()
# print(Mercado_Objetivo,dinero_Disponible,tiempo_De_Compra)
# print(agentecompra.obtener_Lista_Productos())


# Crear la ventana principal de los detalles de compra que se va hacer
detalles = tk.Tk()
# Establecer la posición inicial de la ventana
detalles.geometry("+1100+300")
# Modificar el tamaño de la ventana
detalles.geometry("400x300")
# Mensajes
mensaje1 = "el dinero disponible es : " + str(dinero_Disponible)
mensaje2 = f"Los productos que se quiere comprar son : {listaProductos}"
mensaje3 = "el tiempo disponible en minutos  es : " + str(tiempo_De_Compra)
mensaje4 = "El mercado objetivo es : "+str(Mercado_Objetivo)

# Etiquetas con los mensajes
label1 = tk.Label(detalles, text=mensaje1)
label1.pack()

label2 = tk.Label(detalles, text=mensaje2)
label2.pack()

label3 = tk.Label(detalles, text=mensaje3)
label3.pack()

label4 = tk.Label(detalles, text=mensaje4)
label4.pack()

# Iniciar el bucle de eventos
detalles.mainloop()


""" instanciamos los mercados """
listaLaPampa = []
Arroz = Producto("arroz", 23, 280)
Huevo = Producto("huevo", 23, 60)
Papa = Producto("papa", 23, 28)
Carne = Producto("carne", 23, 35)

listaLaPampa = [Arroz, Huevo, Papa, Carne]


listaSanAntonio = []
Cuaderno = Producto("cuaderno", 100, 12)
Guitarra = Producto("guitarra", 20, 420)
Hilos = Producto("hilos", 100, 2)
Zapatos = Producto("zapatos", 50, 150)

listaSanAntonio = [Cuaderno, Guitarra, Hilos, Zapatos]

listaFidelAranibar = []
Saco = Producto("saco", 100, 350)
Corbata = Producto("guitarra", 20, 25)
Juguete = Producto("hilos", 100, 90)
Torta = Producto("zapatos", 50, 30)

listaFidelAranibar = [Saco, Corbata, Juguete, Torta]


mercado_La_Pampa = Mercado("La Pampa", listaLaPampa)
mercado_San_Antonio = Mercado("San Antonio", listaSanAntonio)
mercado_Fidel_Aranibar = Mercado("Fidel Aranibar",listaFidelAranibar)

# nuevalistapampa = mercado_La_Pampa.obtener_Lista_Productos()
# print(nuevalistapampa[1].get_nombre())

# nuevalistaSanAntonio = mercado_San_Antonio.obtener_Lista_Productos()
# print(nuevalistaSanAntonio[1].get_nombre())


cargarGrafico(primerRuta,segundaRuta)
