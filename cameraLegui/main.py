import cv2
from PIL import Image

from util import get_limits

# Solicitar al usuario que ingrese su nombre
#nombre = input("Por favor, ingresa tu nombre: ")

# Mostrar un saludo personalizado
#print("¡Hola,", nombre, "! Bienvenido.")


# Solicitar al usuario que ingrese los valores RGB separados por comas o espacios
entrada = input("Ingrese los valores RGB (R G B) separados por espacios: ")

# Dividir la entrada en una lista de valores
valores = entrada.split()

# Convertir los valores a enteros
b, g, r = map(int, valores)

# Comprobar si los valores están dentro del rango válido
if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
    dato_color = (r,g,b)
    print("Valores RGB ingresados:", dato_color)
else:
    print("Los valores RGB deben estar en el rango de 0 a 255.")

cap = cv2.VideoCapture(0)

while True:
    ret, display = cap.read()

    hsvImage = cv2.cvtColor(display, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=dato_color)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        display = cv2.rectangle(display, (x1, y1), (x2, y2), (255,255,255), 2)

        # Agregar texto al rectángulo
        text = "Objeto "
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(display, text, (x1, y1 - 10), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow('display', display)

    if cv2.waitKey(1) == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
