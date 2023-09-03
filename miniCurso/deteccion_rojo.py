import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0) # Abrir una cámara web


while True:
    hayvideo, video = cap.read()

    if hayvideo == True:
        cv.imshow(video, "display")
        if cv.waitKey(1) & 0xFF == ord('s'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release() # Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta