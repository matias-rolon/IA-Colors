import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0) # Abrir una cámara web

# Configuro calidad de video
nuevo_ancho = 720
nuevo_alto = 480
video = cv.resize(cap, (nuevo_ancho, nuevo_alto))

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable

# Rangos de Colores
#Rojo
rojo_bajo1 = np.array([], np.uint8)
rojo_alto1 = np.array([], np.uint8)

rojo_bajo2 = np.array([], np.uint8)
rojo_alto2 = np.array([], np.uint8)

while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video

    if hayvideo == True:
        videoHSV = cv.cvtColor(video, cv.COLOR_BGR2HSV)
        mascara_rojo1 = 
        mascara_rojo2 = 
        cv.imshow("Ventana de Visualizacion", video)
        if cv.waitKey(1) & 0xFF == ord('s'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release() # Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta