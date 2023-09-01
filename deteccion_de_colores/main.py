import cv2
import numpy as np
from PIL import Image

# Solicitar al usuario que ingrese los valores RGB separados por comas o espacios
#entrada = input("Ingrese los valores BGR (B G R) separados por espacios: ")
#valores = entrada.split() # Dividir la entrada en una lista de valores
#b, g, r = map(int, valores) # Convertir los valores a enteros

# Comprobar si los valores están dentro del rango válido
#if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
#    dato_color = (b, g ,r)
#    print("Valores RGB ingresados:", dato_color)
#else:
#    print("Los valores RGB deben estar en el rango de 0 a 255.")

cap = cv2.VideoCapture(0) # 0 camara local, 1 camara secundaria(celu), 2(otra), etc...

cap.set(3, 720)  # Configura el ancho del fotograma en píxeles
cap.set(4, 480)  # Configura el alto del fotograma en píxeles

# Tamaño deseado para la ventana de visualización
nuevo_ancho = 720
nuevo_alto = 480
# Cambia el tamaño de la ventana de visualización
cv2.namedWindow("Ventana de Visualizacion", cv2.WINDOW_NORMAL)  # Establece la ventana en modo redimensionable
# Configurar la ventana para que sea redimensionable
cv2.setWindowProperty("Ventana de Visualizacion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    hayvideo, video = cap.read()

    if not hayvideo:
        break

    hsvImage = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # rojo
    rojo_oscuro = np.array([0,0,145])
    rojo_claro = np.array([60,60,255])

    # verde
    verde_oscuro = np.array([0,145,0])
    verde_claro = np.array([60,255,60])

    # azul
    azul_oscuro = np.array([130,0,0])
    azul_claro = np.array([255,60,55])

    # amarillo
    amarillo_oscuro = np.array([0,136,136])
    amarillo_claro = np.array([130,255,255])


    mascara_rojo = cv2.inRange(hsvImage, rojo_oscuro, rojo_claro)
    mascara_verde = cv2.inRange(hsvImage, verde_oscuro, verde_claro)
    mascara_azul = cv2.inRange(hsvImage, azul_oscuro, azul_claro)
    mascara_amarillo = cv2.inRange(hsvImage, amarillo_oscuro, amarillo_claro)



    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        video = cv2.rectangle(video, (x1, y1), (x2, y2), (255,255,255), 2)

        # Agregar texto al rectángulo
        text = "Objeto"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(video, text, (x1, y1 - 10), font, 0.5, dato_color, 1, cv2.LINE_AA)

    cv2.imshow("Ventana de Visualizacion", video)
    k = cv2.waitKey(1)
    if k == 's':
        break

cap.release()
cv2.destroyAllWindows()
