import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable
# Rangos de Colores
#Rojo
NARANJA_MIN = np.array([5, 50, 50],np.uint8)
NARANJA_MAX = np.array([15, 255, 255],np.uint8)

while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video

    if hayvideo:
        hsv_video = cv.cvtColor(video,cv.COLOR_BGR2HSV) # paso el video a HSV(HUE SATURATION VALUE)
        mascaraNaranja = cv.inRange(hsv_video, NARANJA_MIN, NARANJA_MAX) #CREO LAS MASCARAS DE NARANJA

        #MUESTRO POR VENTANA
        cv.imshow('Ventana video Original', video)
        cv.imshow('Ventana video HSV', hsv_video)
        cv.imshow('VENTANA video Resultado', mascaraNaranja)

        if cv.waitKey(1) == ord('s'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release()# Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta