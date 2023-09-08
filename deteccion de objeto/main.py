import cv2 as cv
import numpy as np

DEBUG_HSV = 0
cap = cv.VideoCapture(0)

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable


while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video
    if hayvideo:
        hsv_video = cv.cvtColor(video ,cv.COLOR_BGR2HSV) # paso el video a HSV(HUE SATURATION VALUE)

        #MUESTRO POR VENTANA
        cv.imshow("Ventana de Visualizacion", video)
        if DEBUG_HSV == True :
            cv.imshow('Ventana video ', hsv_video)

        if cv.waitKey(1) == ord('esc'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release()# Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta