import cv2 as cv
import numpy as np
import color as color

DEBUG_HSV = 0
cap = cv.VideoCapture(0)

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable
# Rangos de Colores
#NARANJA
NARANJA_MIN = np.array([12, 100, 100],np.uint8)
NARANJA_MAX = np.array([20, 255, 255],np.uint8)
#AZUL
AZUL_MIN = np.array([110, 100, 20],np.uint8)
AZUL_MAX = np.array([128, 255, 255],np.uint8)
#verde
VERDE_MIN = np.array([45, 40, 70],np.uint8)
VERDE_MAX = np.array([80, 255, 255],np.uint8)

#Rojo
ROJO_BAJO1 = np.array([0,110,26], np.uint8)
ROJO_ALTO1 = np.array([6,255,255], np.uint8)

ROJO_BAJO2 = np.array([177,110,26], np.uint8)
ROJO_ALTO2 = np.array([179,255,255], np.uint8)

while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video
    if hayvideo:
        hsv_video = cv.cvtColor(video ,cv.COLOR_BGR2HSV) # paso el video a HSV(HUE SATURATION VALUE)

        #color naranja
        contornos_naranja = color.convertir(hsv_video, NARANJA_MIN, NARANJA_MAX)
        color.dibujar(contornos_naranja, video, "Objeto Naranja")

        #color azul
        contornos_azul = color.convertir(hsv_video, AZUL_MIN, AZUL_MAX)
        color.dibujar(contornos_azul, video, "Objeto azul")

        #color verde
        contornos_verde = color.convertir(hsv_video, VERDE_MIN, VERDE_MAX)
        color.dibujar(contornos_verde, video, "Objeto verde")

        #MUESTRO POR VENTANA
        cv.imshow("Ventana de Visualizacion", video)
        if DEBUG_HSV == True :
            cv.imshow('Ventana video HSV', hsv_video)

        if cv.waitKey(1) == ord('esc'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release()# Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta