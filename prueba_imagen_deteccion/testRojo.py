import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread("C:/Users/juana/Dropbox/GIT/Sofware/IA-Colors/cameraLegui/imagen.jpg")

if imagen is None:
    print("No se pudo cargar la imagen.")

# Definir los lmites inferior y superior para el color rojo (en formato BGR)
lmite_inferior = np.array([0, 0, 100], dtype=np.uint8)
lmite_superior = np.array([80, 80, 255], dtype=np.uint8)

# Aplicar la segmentación de color
mascara = cv2.inRange(imagen, lmite_inferior, lmite_superior)

# Mostrar la imagen original y la máscara resultante
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Máscara", mascara)

# Esperar a que el usuario presione una tecla y luego cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
