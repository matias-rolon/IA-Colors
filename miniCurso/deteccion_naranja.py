import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX
text = 'Objeto naranja'
# Cambia el tamaño de la ventana de visualización
cv.namedWindow("Ventana de Visualizacion", cv.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable
# Rangos de Colores
#Rojo
NARANJA_MIN = np.array([10, 150, 150],np.uint8)
NARANJA_MAX = np.array([18, 255, 255],np.uint8)

while True:
    hayvideo, video = cap.read() # Obtengo video en vivo si hayvideo es true => hay video

    if hayvideo:
        hsv_video = cv.cvtColor(video,cv.COLOR_BGR2HSV) # paso el video a HSV(HUE SATURATION VALUE)
        mascaraNaranja = cv.inRange(hsv_video, NARANJA_MIN, NARANJA_MAX) #CREO LAS MASCARAS DE NARANJA

        #etapa de contornos
        contornos, _ = cv.findContours(mascaraNaranja, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        #realizamos un filtro para eliminar objetos basura 
        for c in contornos:
            area = cv.contourArea(c)
            if area > 3000:
                contorno_suavisado = cv.convexHull(c)
                cv.drawContours(video ,[contorno_suavisado], 0 , (50,130,255) , 8)
                #cv.putText(video, text, (contorno_suavisado - 20), font, 0.5, (0,0,0), 1, cv.LINE_AA)
        #MUESTRO POR VENTANA
        cv.imshow("Ventana de Visualizacion", video)
        #cv.imshow('Ventana video HSV', hsv_video)
        #cv.imshow('VENTANA video Resultado', mascaraNaranja)

        if cv.waitKey(1) == ord('s'): # Si es presionada durante 1ms la tecla 'S' ord() devuelve el valor que es comparado con waitKey(1) y el programa sale del while
            break

cap.release()# Liberar la captura de video y cerrar la cámara
cv.destroyAllWindows() # Cerrar cualquier ventana abierta