from Productos import *

import tkinter as tk
from tkinter import simpledialog

nombre=""
cantidad=0
precio_unitario=0


# Función para ingresar datos
def ingresar_datos():
    global nombre
    nombre = simpledialog.askstring("Ingreso de datos", "Por favor, ingresa el nombre del producto:")
    global cantidad
    cantidad = simpledialog.askinteger("Ingreso de datos", "Por favor, ingresa la cantidad del producto:")
    global precio_unitario
    precio_unitario = simpledialog.askfloat("Ingreso de datos", "Por favor, ingresa el precio unitario del producto:")
    

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Ingreso de Datos")

# Crear un botón que llame a la función al hacer clic
boton_ingresar = tk.Button(ventana, text="Ingresar Datos", command=ingresar_datos)
boton_ingresar.pack(pady=20)

# Ejemplo de uso
ventana.mainloop()


# Crear un objeto Producto con los valores ingresados
producto1 = Producto(nombre, cantidad, precio_unitario)

# Acceder y actualizar atributos utilizando los métodos get y set
print("Producto 1:")
print("Nombre:", producto1.get_nombre())
print("Cantidad:", producto1.get_cantidad())
print("Precio Unitario:", producto1.get_precio_unitario())
# print("Total:", producto1.calcular_total())
