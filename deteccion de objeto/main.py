import cv2 as cv
import numpy as np

DEBUG_HSV = 0
cap = cv.VideoCapture(0)

# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Capturacion de objeto", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable


while True:
    hayvideo, video1 = cap.read() # Obtengo video en vivo si hayvideo es true => hay video
    cv.imshow("Ventana de Capturacion de objeto", video1)  #MUESTRO POR VENTANA
    if cv.waitKey(1) == ord('c'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break
    
# Leemos ultima img y la guardamos
objeto = cv.imread('objeto1.jpg', 0)
recorte= objeto[160:300, 230:380]
cv.imshow(" recorte de objeto",recorte)

while True:
    hayvideo, video2 = cap.read() # Obtengo video en vivo si hayvideo es true => hay video
    cv.imshow("Deteccion", video2)  #MUESTRO POR VENTANA
cap.release()# Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta