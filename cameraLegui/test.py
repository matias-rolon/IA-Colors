import cv2

cap = cv2.VideoCapture(0)  # Abre la cámara con índice 0 (cámara predeterminada)

while True:
    hayvideo, video = cap.read()  # Lee un video de la cámara
    videorgb = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    if not hayvideo:
        break

    cv2.imshow('Camera Feed', videorgb)  # Muestra el video en una ventana llamada "Camera Feed"

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()  # Libera la cámara
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas
