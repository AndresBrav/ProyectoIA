from GraficarCamino import cargarGrafico
from Rutas import *
from Productos import *
from Mercado import *
import tkinter as tk
from tkinter import simpledialog


""" el usuario introduce cuánto dinero tendrá
el agente para el transporte(Tanto de ida, y vuelta), que productos debe comprar. Y
también el usuario introduce el tiempo que debe tardar en su compra. """
dinero_Disponible = 0
listaProductos = []
tiempo_De_Compra = 0


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
            # Agregar el producto a  a la lista
            listaProductos.append(str(producto))

        global tiempo_De_Compra
        tiempo_De_Compra = simpledialog.askfloat(
            "Ingreso de datos",
            "Por favor, ingresa el tiempo que vas a tardar en comprar en minutos:",
        )
        # print(dinero_Disponible,listaProductos,tiempo_De_Compra)
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


# print(dinero_Disponible)
# print(listaProductos)
# print(tiempo_De_Compra)

"""instanciamos las rutas que vamos usar"""
# Rutas(nombre,tiempoRecorridoMinutos,distanciaMetros,pasaje)
Ruta1 = Rutas("graficarRuta1", 34, 1700, 1.7)
Ruta2LaPampa = Rutas("ruta2LaPampa", 58, 2900, 2.9)
Ruta3SanAntonio = Rutas("ruta3SanAntonio", 20, 1000, 1)
Ruta4 = Rutas("ruta4", 8, 400, 0.4)
Ruta4FidelAranibar = Rutas("ruta4FidelAranibar", 24, 1200, 1.2)
Ruta5SanAntonio = Rutas("ruta5SanAntonio", 80, 4000, 4)
Ruta5LaPampa = Rutas("ruta5LaPampa", 98, 4900, 4.9)

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

listaFidelAranibar = [Saco,Corbata,Juguete,Torta]


mercado_La_Pampa = Mercado("La Pampa", listaLaPampa)
mercado_San_Antonio=Mercado("San Antonio",listaSanAntonio)

nuevalistapampa = mercado_La_Pampa.obtener_Lista_Productos()
print(nuevalistapampa[1].get_nombre())

nuevalistaSanAntonio = mercado_San_Antonio.obtener_Lista_Productos()
print(nuevalistaSanAntonio[1].get_nombre())


cargarGrafico()
