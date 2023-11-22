import cv2

# def cargarGrafico(listaRecorrido):


def cargarGrafico():
    img = cv2.imread("MapaIA6.png")
    # lista=listaRecorrido
    # dist=0
    # tiempo=0
    try:
        GraficarCuadrantes(img)
    except Exception:
        print("problemas al graficar")

    

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def GraficarCuadrantes(img):
    try:
        Main1(img)
    except:
        print("no grafico")

def Main1(img):
    pintarHorizontal(img,55,50,45,10)

def pintarHorizontal(img,iniX,largo,iniY,ancho): 
    try:
        for i in range(iniX,iniX + largo):
            for j in range (iniY,iniY+ancho):
                img[j,i]=(0,0,255) 
    except Exception:
        print("error")
    
         
def pintarvertical(img,iniX,largo,iniY,ancho): 
    try:
        for i in range(iniY,iniY + largo):
            for j in range (iniX,iniX+ancho):
                img[i,j]=(0,0,255) 
    except Exception:
        print("error")

cargarGrafico()

# pip install opencv-python tienes que instalar

