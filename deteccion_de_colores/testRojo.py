import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.VideoCapture(0)

# Definir los limites inferior y superior para el color rojo (en formato BGR)
limite_inferior = np.array([0, 0, 100], dtype=np.uint8)
limite_superior = np.array([80, 80, 255], dtype=np.uint8)

# Aplicar la segmentación de color
máscara = cv2.inRange(imagen, limite_inferior, limite_superior)

# Mostrar la imagen original y la máscara resultante
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Máscara", máscara)

# Esperar a que el usuario presione una tecla y luego cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
