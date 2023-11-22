import cv2

# def cargarGrafico(listaRecorrido):
print(cv2.__version__)


def cargarGrafico():
    img = cv2.imread("MapaIA6.png")
    # lista=listaRecorrido
    # dist=0
    # tiempo=0
    try:
        for i in range(50, 100):
            img[133, i] = (0, 0, 255)
            img[134, i] = (0, 0, 255)
            img[135, i] = (0, 0, 255)
            img[136, i] = (0, 0, 255)
            img[137, i] = (0, 0, 255)
    except Exception:
        print("problemas al graficar")

     # Escribir texto en una posición específica
    font = cv2.FONT_HERSHEY_SIMPLEX
    posicion_texto = (50, 100)  # Posición (x, y) donde se colocará el texto
    texto = "Texto de ejemplo"
    color_texto = (0,0,0)  # Color del texto en formato BGR

    cv2.putText(img, texto, posicion_texto, font, 1, color_texto, 2, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cargarGrafico()

# pip install opencv-python tienes que instalar

