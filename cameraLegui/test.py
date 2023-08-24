import cv2

cap = cv2.VideoCapture(0)  # Abre la cámara con índice 0 (cámara predeterminada)

while True:
    ret, frame = cap.read()  # Lee un frame de la cámara

    if not ret:
        break

    cv2.imshow('Camera Feed', frame)  # Muestra el frame en una ventana llamada "Camera Feed"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Libera la cámara
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas
