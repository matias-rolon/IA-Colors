import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0) # Abrir una cámara web

# Configuro calidad de video
nuevo_ancho = 720
nuevo_alto = 480

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable
# Rangos de Colores
#Rojo
rojo_bajo1 = np.array([0,110,26], np.uint8)
rojo_alto1 = np.array([6,255,255], np.uint8)

rojo_bajo2 = np.array([177,110,26], np.uint8)
rojo_alto2 = np.array([179,255,255], np.uint8)

while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video
    video_redimensionado = cv.resize(video, (nuevo_ancho, nuevo_alto))

    if hayvideo == True:
        videoHSV = cv.cvtColor(video_redimensionado, cv.COLOR_RGB2HSV) # paso el video a HSV(HUE SATURATION VALUE)
        mascara_rojo1 = cv.inRange( videoHSV, rojo_bajo1, rojo_alto1) #CREO LAS MASCARAS DE ROJO
        mascara_rojo2 = cv.inRange( videoHSV, rojo_bajo2, rojo_alto2)
        mascara_rojo = cv.add(mascara_rojo1, mascara_rojo2)

        cv.imshow('ventana hsv', videoHSV)
        cv.imshow('Ventana para ver resultado', mascara_rojo)
        cv.imshow("Ventana de Visualizacion", video)
        if cv.waitKey(1) & 0xFF == ord('s'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release() # Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta