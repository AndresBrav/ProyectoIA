import cv2

# def cargarGrafico(listaRecorrido):
# from Productos import *
# import tkinter as tk
# from tkinter import simpledialog


# """ el usuario introduce cuánto dinero tendrá
# el agente para el transporte(Tanto de ida, y vuelta), que productos debe comprar. Y
# también el usuario introduce el tiempo que debe tardar en su compra. """
# dinero_Disponible = 0
# listaProductos = []
# tiempo_De_Compra = 0


# # Función para ingresar datos
# def ingresar_datos():
#     try:
#         global dinero_Disponible
#         dinero_Disponible = simpledialog.askfloat(
#             "Ingreso de datos", "Por favor, ingresa el dinero disponible para el viaje"
#         )

#         # Crear una lista para almacenar las cantidades de productos
#         global listaProductos
#         listaProductos = []

#         # Solicitar al usuario que ingrese la cantidad de productos
#         while True:
#             producto = simpledialog.askstring(
#                 "Ingreso de datos",
#                 "Por favor, ingresa el producto (o introduce la palabra (stop) para terminar):",
#             )

#             # Si el producto  es stop, salir del bucle
#             if producto == "stop":
#                 break
#             # Agregar el producto a  a la lista
#             listaProductos.append(str(producto))

#         global tiempo_De_Compra
#         tiempo_De_Compra = simpledialog.askfloat(
#             "Ingreso de datos",
#             "Por favor, ingresa el tiempo que vas a tardar en comprar en minutos:",
#         )
#         # print(dinero_Disponible,listaProductos,tiempo_De_Compra)
#     except (ValueError, TypeError):
#         print("Error: Ingresa un valor numérico válido.")


# # Crear una ventana principal
# ventana = tk.Tk()
# ventana.title("Ejemplo de Ingreso de Datos")
# # Modificar el tamaño de la ventana
# ventana.geometry("400x300")
# # Cambiar el color de fondo de la ventana
# ventana.configure(bg="#FFFFFF")

# # Crear un botón que llame a la función al hacer clic
# boton_ingresar = tk.Button(
#     ventana,
#     text="Ingresar Datos",
#     command=ingresar_datos,
#     font=("Arial", 14),
#     bg="#FFFFFF",  # Cambiar el color de fondo del botón
#     fg="black",  # Cambiar el color del texto del botón
#     padx=20,  # Añadir relleno horizontal
#     pady=10,  # Añadir relleno vertical)
# )
# boton_ingresar.pack(pady=20)
# # Ejemplo de uso
# ventana.mainloop()


# print(dinero_Disponible)
# print(listaProductos)
# print(tiempo_De_Compra)


# def cargarGrafico(numero):
def cargarGrafico():
    img = cv2.imread("MapaCocha7.png")
    # lista=listaRecorrido
    # dist=0
    # tiempo=0
    try:
        # GraficarCuadrantes(img)
        GraficarRutas(img)
    except Exception:
        print("problemas al graficar")

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def GraficarRutas(img):
    # GraficarRuta1(img)
    # GraficarRuta2LaPampa(img)
    # GraficarRuta3SanAntonio(img)
    # GraficarRuta4(img)
    # GraficarRuta4FidelAranibar(img)
    # GraficarRuta5SanAntonio(img)
    GraficarRuta5LaPampa(img)


def GraficarRuta1(img):
    Brasil10(img)
    Brasil11(img)
    Brasil12(img)
    Brasil13(img)

    EstebanArce3(img)
    EstebanArce4(img)
    EstebanArce5(img)

    Aroma6(img)
    Aroma7(img)
    Aroma8(img)
    Aroma9(img)

    NatanielAguirre3(img)
    NatanielAguirre4(img)
    NatanielAguirre5(img)
    NatanielAguirre6(img)
    NatanielAguirre7(img)
    NatanielAguirre8(img)


def GraficarRuta2SanAntonio(img):
    IsmaelMontes2(img)
    IsmaelMontes4(img)
    IsmaelMontes5(img)

    Ayacucho8(img)
    Ayacucho9(img)
    Ayacucho10(img)
    Ayacucho11(img)
    Ayacucho12(img)
    Ayacucho13(img)
    Ayacucho14(img)

    Punata2(img)
    Punata4(img)
    Punata5(img)
    Punata6(img)
    Punata7(img)
    Punata8(img)
    Punata9(img)
    Punata10(img)


def GraficarRuta2LaPampa(img):
    IsmaelMontes2(img)
    IsmaelMontes4(img)
    IsmaelMontes5(img)

    Ayacucho8(img)
    Ayacucho9(img)
    Ayacucho10(img)
    Ayacucho11(img)
    Ayacucho12(img)
    Ayacucho13(img)
    Ayacucho14(img)

    Punata2(img)
    Punata4(img)
    Punata5(img)
    Punata6(img)
    Punata7(img)
    Punata8(img)
    Punata9(img)
    Punata10(img)
    Punata11(img)
    Punata12(img)
    Punata13(img)
    Punata14(img)
    Punata15(img)
    Punata16(img)
    Punata17(img)
    Punata19(img)
    Barrientos14(img)
    AgustinLopez8(img)
    AgustinLopez14(img)


def GraficarRuta3SanAntonio(img):
    NatanielAguirre9(img)
    NatanielAguirre10(img)
    NatanielAguirre11(img)
    NatanielAguirre12(img)
    NatanielAguirre13(img)

    Punata6(img)
    Punata7(img)
    Punata8(img)
    Punata9(img)
    Punata10(img)


def GraficarRuta4(img):
    Mayo5(img)
    Mayo6(img)
    Mayo7(img)
    Mayo8(img)


def GraficarRuta4FidelAranibar(img):
    Mayo9(img)
    Mayo10(img)
    Mayo11(img)
    Mayo12(img)
    Mayo13(img)

    Punata12(img)
    Punata13(img)
    Punata14(img)

    FrVal(img)

    Tarata12(img)
    Tarata13(img)
    Tarata14(img)


def GraficarRuta5SanAntonio(img):
    IsmaelMontes10(img)
    IsmaelMontes11(img)
    IsmaelMontes12(img)
    IsmaelMontes13(img)

    EstebanArce31(img)
    EstebanArce41(img)
    EstebanArce51(img)
    EstebanArce6(img)
    EstebanArce7(img)
    EstebanArce8(img)

    Aroma1(img)
    Aroma2(img)
    Aroma3(img)
    Aroma4(img)
    Aroma5(img)
    Aroma61(img)
    Aroma71(img)
    Aroma81(img)
    Aroma91(img)

    Ayacucho3(img)
    Ayacucho4(img)
    Ayacucho5(img)
    Ayacucho6(img)
    Ayacucho7(img)
    Ayacucho8(img)
    Ayacucho9(img)
    Ayacucho10(img)
    Ayacucho11(img)
    Ayacucho12(img)
    Ayacucho13(img)
    Ayacucho14(img)

    Punata2(img)
    Punata4(img)
    Punata5(img)
    Punata6(img)
    Punata7(img)
    Punata8(img)
    Punata9(img)
    Punata10(img)
    AgustinLopez14(img)


def GraficarRuta5LaPampa(img):
    IsmaelMontes10(img)
    IsmaelMontes11(img)
    IsmaelMontes12(img)
    IsmaelMontes13(img)

    EstebanArce31(img)
    EstebanArce41(img)
    EstebanArce51(img)
    EstebanArce6(img)
    EstebanArce7(img)
    EstebanArce8(img)

    Aroma1(img)
    Aroma2(img)
    Aroma3(img)
    Aroma4(img)
    Aroma5(img)
    Aroma61(img)
    Aroma71(img)
    Aroma81(img)
    Aroma91(img)

    Ayacucho3(img)
    Ayacucho4(img)
    Ayacucho5(img)
    Ayacucho6(img)
    Ayacucho7(img)
    Ayacucho8(img)
    Ayacucho9(img)
    Ayacucho10(img)
    Ayacucho11(img)
    Ayacucho12(img)
    Ayacucho13(img)
    Ayacucho14(img)

    Punata2(img)
    Punata4(img)
    Punata5(img)
    Punata6(img)
    Punata7(img)
    Punata8(img)
    Punata9(img)
    Punata10(img)
    Punata10(img)
    Punata11(img)
    Punata12(img)
    Punata13(img)
    Punata14(img)
    Punata15(img)
    Punata16(img)
    Punata17(img)
    Punata19(img)
    Barrientos14(img)
    AgustinLopez14(img)


def FrVal(img):
    pintarverticalNaranja(img, 650, 60, 610, 30)


def Aroma1(img):
    pintarHorizontalNaranja(img, 10, 50, 90, 20)


""" + 55 """


def Aroma2(img):
    pintarHorizontalNaranja(img, 65, 50, 90, 20)


def Aroma3(img):
    pintarHorizontalNaranja(img, 120, 50, 90, 20)


""" + 60 """


def Aroma4(img):
    pintarHorizontalNaranja(img, 180, 50, 90, 20)


def Aroma5(img):
    pintarHorizontalNaranja(img, 240, 50, 90, 20)


def Aroma6(img):
    pintarHorizontalNegro(img, 295, 50, 90, 20)


""" + 60 """


def Aroma7(img):
    pintarHorizontalNegro(img, 355, 50, 90, 20)


def Aroma8(img):
    pintarHorizontalNegro(img, 410, 50, 90, 20)


def Aroma9(img):
    pintarHorizontalNegro(img, 465, 50, 90, 20)


def Aroma61(img):
    pintarHorizontalNaranja(img, 295, 50, 90, 20)


""" + 60 """


def Aroma71(img):
    pintarHorizontalNaranja(img, 355, 50, 90, 20)


def Aroma81(img):
    pintarHorizontalNaranja(img, 410, 50, 90, 20)


def Aroma91(img):
    pintarHorizontalNaranja(img, 465, 50, 90, 20)


""" + 60 """


def Aroma10(img):
    pintarHorizontal(img, 525, 50, 90, 20)


def Aroma11(img):
    pintarHorizontal(img, 585, 50, 90, 20)


def Aroma12(img):
    pintarHorizontal(img, 645, 50, 90, 20)


""" + 55 """


def Aroma13(img):
    pintarHorizontal(img, 700, 50, 90, 20)


def Aroma14(img):
    pintarHorizontal(img, 755, 50, 90, 20)


def Aroma15(img):
    pintarHorizontal(img, 810, 50, 90, 20)


""" + 55 """


def Aroma16(img):
    pintarHorizontal(img, 865, 50, 90, 20)


def Aroma17(img):
    pintarHorizontal(img, 920, 50, 90, 20)


def Aroma18(img):
    pintarHorizontal(img, 985, 50, 90, 20)


def Aroma19(img):
    pintarHorizontal(img, 1040, 50, 90, 20)


def Aroma20(img):
    pintarHorizontal(img, 1095, 50, 90, 20)


""" calle Brasil """


def Brasil10(img):
    pintarHorizontalNegro(img, 525, 50, 230, 20)


def Brasil11(img):
    pintarHorizontalNegro(img, 585, 50, 230, 20)


def Brasil12(img):
    pintarHorizontalNegro(img, 645, 50, 230, 20)


""" + 55 """


def Brasil13(img):
    pintarHorizontalNegro(img, 700, 50, 230, 20)


def Brasil14(img):
    pintarHorizontal(img, 755, 50, 230, 20)


def Brasil15(img):
    pintarHorizontal(img, 810, 50, 230, 20)


""" + 55 """


def Brasil16(img):
    pintarHorizontal(img, 865, 50, 230, 20)


def Brasil17(img):
    pintarHorizontal(img, 920, 50, 230, 20)


def Brasil19(img):
    pintarHorizontal(img, 1040, 50, 230, 20)


def Brasil20(img):
    pintarHorizontal(img, 1095, 50, 230, 20)


""" Calle Ismael Montes """


def IsmaelMontes2(img):
    pintarHorizontalNaranja(img, 70, 50, 345, 20)


def IsmaelMontes4(img):
    pintarHorizontalNaranja(img, 180, 50, 345, 20)


def IsmaelMontes5(img):
    pintarHorizontalNaranja(img, 240, 50, 345, 20)


def IsmaelMontes6(img):
    pintarHorizontal(img, 295, 50, 345, 20)


""" + 60 """


def IsmaelMontes7(img):
    pintarHorizontal(img, 355, 50, 345, 20)


def IsmaelMontes8(img):
    pintarHorizontal(img, 410, 50, 345, 20)


def IsmaelMontes9(img):
    pintarHorizontal(img, 465, 50, 345, 20)


""" + 60 """


def IsmaelMontes10(img):
    pintarHorizontalNaranja(img, 525, 50, 345, 20)


def IsmaelMontes11(img):
    pintarHorizontalNaranja(img, 585, 50, 345, 20)


def IsmaelMontes12(img):
    pintarHorizontalNaranja(img, 645, 50, 345, 20)


""" + 55 """


def IsmaelMontes13(img):
    pintarHorizontalNaranja(img, 700, 50, 345, 20)


def IsmaelMontes14(img):
    pintarHorizontal(img, 755, 50, 345, 20)


def IsmaelMontes15(img):
    pintarHorizontal(img, 810, 50, 345, 20)


""" + 55 """


def IsmaelMontes16(img):
    pintarHorizontal(img, 865, 50, 345, 20)


def IsmaelMontes17(img):
    pintarHorizontal(img, 920, 50, 345, 20)


""" Calle Honduras """


def Honduras4(img):
    pintarHorizontal(img, 180, 50, 460, 20)


def Honduras5(img):
    pintarHorizontal(img, 240, 50, 460, 20)


def Honduras6(img):
    pintarHorizontal(img, 295, 50, 460, 20)


""" + 60 """


def Honduras7(img):
    pintarHorizontal(img, 355, 50, 460, 20)


def Honduras8(img):
    pintarHorizontal(img, 410, 50, 460, 20)


def Honduras9(img):
    pintarHorizontal(img, 465, 50, 460, 20)


""" + 60 """


def Honduras10(img):
    pintarHorizontal(img, 525, 50, 460, 20)


def Honduras11(img):
    pintarHorizontal(img, 585, 50, 460, 20)


def Honduras12(img):
    pintarHorizontal(img, 645, 50, 460, 20)


""" + 55 """


def Honduras13(img):
    pintarHorizontal(img, 700, 50, 460, 20)


def Honduras14(img):
    pintarHorizontal(img, 755, 50, 460, 20)


def Honduras15(img):
    pintarHorizontal(img, 810, 50, 460, 20)


""" + 55 """


def Honduras16(img):
    pintarHorizontal(img, 865, 50, 460, 20)


def Honduras17(img):
    pintarHorizontal(img, 920, 50, 460, 20)


def Honduras19(img):
    pintarHorizontal(img, 1040, 50, 460, 20)


def Honduras20(img):
    pintarHorizontal(img, 1095, 50, 460, 20)


""" Calle Punata """


def Punata2(img):
    pintarHorizontalNaranja(img, 65, 50, 575, 20)


def Punata4(img):
    pintarHorizontalNaranja(img, 180, 50, 575, 20)


def Punata5(img):
    pintarHorizontalNaranja(img, 240, 50, 575, 20)


def Punata6(img):
    pintarHorizontalNaranja(img, 295, 50, 575, 20)


""" + 60 """


def Punata7(img):
    pintarHorizontalNaranja(img, 355, 50, 575, 20)


def Punata8(img):
    pintarHorizontalNaranja(img, 410, 50, 575, 20)


def Punata9(img):
    pintarHorizontalNaranja(img, 465, 50, 575, 20)


""" + 60 """


def Punata10(img):
    pintarHorizontalNaranja(img, 525, 50, 575, 20)


def Punata11(img):
    pintarHorizontalNaranja(img, 585, 50, 575, 20)


def Punata12(img):
    pintarHorizontalNaranja(img, 645, 50, 575, 20)


""" + 55 """


def Punata13(img):
    pintarHorizontalNaranja(img, 700, 50, 575, 20)


def Punata14(img):
    pintarHorizontalNaranja(img, 755, 50, 575, 20)


def Punata15(img):
    pintarHorizontalNaranja(img, 810, 50, 575, 20)


""" + 55 """


def Punata16(img):
    pintarHorizontalNaranja(img, 865, 50, 575, 20)


def Punata17(img):
    pintarHorizontalNaranja(img, 920, 50, 575, 20)


def Punata19(img):
    pintarHorizontalNaranja(img, 1040, 50, 575, 20)


def Punata20(img):
    pintarHorizontalNaranja(img, 1095, 50, 575, 20)

    """ calle tarata """


def Tarata10(img):
    pintarHorizontal(img, 525, 50, 690, 20)


def Tarata11(img):
    pintarHorizontal(img, 585, 50, 690, 20)


def Tarata12(img):
    pintarHorizontalNaranja(img, 645, 50, 690, 20)


""" + 55 """


def Tarata13(img):
    pintarHorizontalNaranja(img, 700, 50, 690, 20)


def Tarata14(img):
    pintarHorizontalNaranja(img, 755, 50, 690, 20)


def Tarata15(img):
    pintarHorizontal(img, 810, 50, 690, 20)


""" + 55 """


def Tarata16(img):
    pintarHorizontal(img, 865, 50, 690, 20)


def Tarata17(img):
    pintarHorizontal(img, 920, 50, 690, 20)


def Ayacucho1(img):
    pintarvertical(img, 25, 30, 10, 20)


""" +40 """


def Ayacucho2(img):
    pintarvertical(img, 25, 30, 50, 20)


def Ayacucho3(img):
    pintarverticalNaranja(img, 25, 30, 140, 20)


def Ayacucho4(img):
    pintarverticalNaranja(img, 25, 30, 190, 20)


def Ayacucho5(img):
    pintarverticalNaranja(img, 25, 25, 230, 20)


def Ayacucho6(img):
    pintarverticalNaranja(img, 25, 25, 270, 20)


def Ayacucho7(img):
    pintarverticalNaranja(img, 25, 25, 305, 20)


def Ayacucho8(img):
    pintarverticalNaranja(img, 25, 25, 340, 20)


def Ayacucho9(img):
    pintarverticalNaranja(img, 25, 25, 375, 20)


def Ayacucho10(img):
    pintarverticalNaranja(img, 25, 25, 420, 20)


def Ayacucho11(img):
    pintarverticalNaranja(img, 25, 25, 460, 20)


def Ayacucho12(img):
    pintarverticalNaranja(img, 25, 25, 495, 20)


def Ayacucho13(img):
    pintarverticalNaranja(img, 25, 25, 535, 20)


def Ayacucho14(img):
    pintarverticalNaranja(img, 25, 25, 570, 20)


def Ayacucho15(img):
    pintarvertical(img, 25, 25, 610, 20)


def Ayacucho16(img):
    pintarvertical(img, 25, 25, 650, 20)


def Ayacucho17(img):
    pintarvertical(img, 25, 25, 690, 20)


def Ayacucho18(img):
    pintarvertical(img, 25, 25, 730, 20)


def Ayacucho19(img):
    pintarvertical(img, 25, 25, 765, 20)


def AgustinLopez1(img):
    pintarvertical(img, 135, 30, 10, 20)


def AgustinLopez2(img):
    pintarvertical(img, 135, 30, 50, 20)


def AgustinLopez3(img):
    pintarvertical(img, 135, 30, 140, 20)


def AgustinLopez4(img):
    pintarvertical(img, 135, 30, 190, 20)


def AgustinLopez5(img):
    pintarvertical(img, 135, 25, 230, 20)


def AgustinLopez6(img):
    pintarvertical(img, 135, 25, 270, 20)


def AgustinLopez7(img):
    pintarvertical(img, 135, 25, 305, 20)


def AgustinLopez8(img):
    pintarverticalNaranja(img, 135, 25, 340, 20)


def AgustinLopez9(img):
    pintarvertical(img, 135, 25, 375, 20)


def AgustinLopez10(img):
    pintarvertical(img, 135, 25, 420, 20)


def AgustinLopez11(img):
    pintarvertical(img, 135, 25, 460, 20)


def AgustinLopez12(img):
    pintarvertical(img, 135, 25, 495, 20)


def AgustinLopez13(img):
    pintarvertical(img, 135, 25, 535, 20)


def AgustinLopez14(img):
    pintarverticalNaranja(img, 135, 25, 570, 20)


def AgustinLopez15(img):
    pintarvertical(img, 135, 25, 610, 20)


def AgustinLopez16(img):
    pintarvertical(img, 135, 25, 650, 20)


def AgustinLopez17(img):
    pintarvertical(img, 135, 25, 690, 20)


def AgustinLopez18(img):
    pintarvertical(img, 135, 25, 730, 20)


def AgustinLopez19(img):
    pintarvertical(img, 135, 25, 765, 20)


def NatanielAguirre1(img):
    pintarvertical(img, 310, 30, 10, 20)


def NatanielAguirre2(img):
    pintarvertical(img, 310, 30, 50, 20)


def NatanielAguirre3(img):
    pintarverticalNegro(img, 310, 30, 140, 20)


def NatanielAguirre4(img):
    pintarverticalNegro(img, 310, 30, 190, 20)


def NatanielAguirre5(img):
    pintarverticalNegro(img, 310, 25, 230, 20)


def NatanielAguirre6(img):
    pintarverticalNegro(img, 310, 25, 270, 20)


def NatanielAguirre7(img):
    pintarverticalNegro(img, 310, 25, 305, 20)


def NatanielAguirre8(img):
    pintarverticalNegro(img, 310, 25, 340, 20)


def NatanielAguirre9(img):
    pintarverticalNaranja(img, 310, 25, 375, 20)


def NatanielAguirre10(img):
    pintarverticalNaranja(img, 310, 25, 420, 20)


def NatanielAguirre11(img):
    pintarverticalNaranja(img, 310, 25, 460, 20)


def NatanielAguirre12(img):
    pintarverticalNaranja(img, 310, 25, 495, 20)


def NatanielAguirre13(img):
    pintarverticalNaranja(img, 310, 25, 535, 20)


def EstebanArce1(img):
    pintarvertical(img, 485, 30, 10, 20)


""" +40 """


def EstebanArce2(img):
    pintarvertical(img, 485, 30, 50, 20)


def EstebanArce3(img):
    pintarverticalNegro(img, 485, 30, 140, 20)


def EstebanArce4(img):
    pintarverticalNegro(img, 485, 30, 190, 20)


def EstebanArce5(img):
    pintarverticalNegro(img, 485, 25, 230, 20)


def EstebanArce31(img):
    pintarverticalNaranja(img, 485, 30, 140, 20)


def EstebanArce41(img):
    pintarverticalNaranja(img, 485, 30, 190, 20)


def EstebanArce51(img):
    pintarverticalNaranja(img, 485, 25, 230, 20)


def EstebanArce6(img):
    pintarverticalNaranja(img, 485, 25, 270, 20)


def EstebanArce7(img):
    pintarverticalNaranja(img, 485, 25, 305, 20)


def EstebanArce8(img):
    pintarverticalNaranja(img, 485, 25, 340, 20)


def EstebanArce9(img):
    pintarvertical(img, 485, 25, 375, 20)


def EstebanArce10(img):
    pintarvertical(img, 485, 25, 420, 20)


def EstebanArce11(img):
    pintarvertical(img, 485, 25, 460, 20)


def EstebanArce12(img):
    pintarvertical(img, 485, 25, 495, 20)


def EstebanArce13(img):
    pintarvertical(img, 485, 25, 535, 20)


def EstebanArce14(img):
    pintarvertical(img, 485, 25, 570, 20)


def EstebanArce15(img):
    pintarvertical(img, 485, 25, 610, 20)


def EstebanArce16(img):
    pintarvertical(img, 485, 25, 650, 20)


def EstebanArce17(img):
    pintarvertical(img, 485, 25, 690, 20)


def EstebanArce18(img):
    pintarvertical(img, 485, 25, 730, 20)


def EstebanArce19(img):
    pintarvertical(img, 485, 25, 765, 20)


def Mayo1(img):
    pintarvertical(img, 770, 30, 10, 20)


def Mayo2(img):
    pintarvertical(img, 770, 30, 50, 20)


def Mayo3(img):
    pintarvertical(img, 770, 30, 140, 20)


def Mayo4(img):
    pintarvertical(img, 770, 30, 190, 20)


def Mayo5(img):
    pintarverticalNegro(img, 770, 25, 230, 20)


def Mayo6(img):
    pintarverticalNegro(img, 770, 25, 270, 20)


def Mayo7(img):
    pintarverticalNegro(img, 770, 25, 305, 20)


def Mayo8(img):
    pintarverticalNegro(img, 770, 25, 340, 20)


def Mayo9(img):
    pintarverticalNaranja(img, 770, 25, 375, 20)


def Mayo10(img):
    pintarverticalNaranja(img, 770, 25, 420, 20)


def Mayo11(img):
    pintarverticalNaranja(img, 770, 25, 460, 20)


def Mayo12(img):
    pintarverticalNaranja(img, 770, 25, 495, 20)


def Mayo13(img):
    pintarverticalNaranja(img, 770, 25, 535, 20)


def SanMartin1(img):
    pintarvertical(img, 1000, 30, 10, 20)


def SanMartin2(img):
    pintarvertical(img, 1000, 30, 50, 20)


def SanMartin3(img):
    pintarvertical(img, 1000, 30, 140, 20)


def SanMartin4(img):
    pintarvertical(img, 1000, 30, 190, 20)


def SanMartin5(img):
    pintarvertical(img, 1000, 25, 230, 20)


def SanMartin6(img):
    pintarvertical(img, 1000, 25, 270, 20)


def SanMartin7(img):
    pintarvertical(img, 1000, 25, 305, 20)


def SanMartin8(img):
    pintarvertical(img, 1000, 25, 340, 20)


def SanMartin9(img):
    pintarvertical(img, 1000, 25, 375, 20)


def SanMartin10(img):
    pintarvertical(img, 1000, 25, 420, 20)


def Barrientos11(img):
    pintarvertical(img, 1000, 25, 460, 20)


def Barrientos12(img):
    pintarvertical(img, 1000, 25, 495, 20)


def Barrientos13(img):
    pintarvertical(img, 1000, 25, 535, 20)


def Barrientos14(img):
    pintarverticalNaranja(img, 1000, 25, 570, 20)


def Barrientos15(img):
    pintarvertical(img, 1000, 25, 610, 20)


def Barrientos16(img):
    pintarvertical(img, 1000, 25, 650, 20)


def Barrientos17(img):
    pintarvertical(img, 1000, 25, 690, 20)


def Barrientos18(img):
    pintarvertical(img, 1000, 25, 730, 20)


def Barrientos19(img):
    pintarvertical(img, 1000, 25, 765, 20)


def pintarHorizontal(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniX, iniX + largo):
            for j in range(iniY, iniY + ancho):
                img[j, i] = (0, 0, 255)
    except Exception:
        print("error")


def pintarHorizontalNaranja(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniX, iniX + largo):
            for j in range(iniY, iniY + ancho):
                # img[j, i] = (0, 165, 255)
                img[j, i] = (9, 124, 242)
    except Exception:
        print("error")


def pintarHorizontalNegro(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniX, iniX + largo):
            for j in range(iniY, iniY + ancho):
                img[j, i] = (0, 0, 0)
    except Exception:
        print("error")


def pintarvertical(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniY, iniY + largo):
            for j in range(iniX, iniX + ancho):
                img[i, j] = (0, 0, 255)
    except Exception:
        print("error")


def pintarverticalNaranja(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniY, iniY + largo):
            for j in range(iniX, iniX + ancho):
                img[i, j] = (9, 124, 242)
    except Exception:
        print("error")


def pintarverticalNegro(img, iniX, largo, iniY, ancho):
    try:
        for i in range(iniY, iniY + largo):
            for j in range(iniX, iniX + ancho):
                img[i, j] = (0, 0, 0)
    except Exception:
        print("error")


# cargarGrafico()

# pip install opencv-python tienes que instalar
