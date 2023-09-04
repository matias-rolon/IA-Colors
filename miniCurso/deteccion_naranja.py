import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

NARANJA_MIN = np.array([5, 50, 50],np.uint8)
NARANJA_MAX = np.array([15, 255, 255],np.uint8)

while True:
    hayvideo, video = cap.read()
    if hayvideo:
        hsv_video = cv.cvtColor(video,cv.COLOR_BGR2HSV)

        frame_threshed = cv.inRange(hsv_video, NARANJA_MIN, NARANJA_MAX)
        cv.imshow('VIDEO', frame_threshed)
        if cv.waitKey(1) == ord('s'):
            break

cap.release()
cv.destroyAllWindows()