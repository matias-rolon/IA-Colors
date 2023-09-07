import cv2 as cv

def convertir(src, bajos , altos):
    mascaraNaranja = cv.inRange(src , bajos, altos) #CREO LAS MASCARAS DE NARANJA
    #etapa de contornos
    contornos, _ = cv.findContours(mascaraNaranja, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contornos

def dibujar(contornos, video, text):
        #realizamos un filtro para eliminar objetos basura 
        for c in contornos:
            area = cv.contourArea(c)
            if area > 2000:
                M = cv.moments(c)
                if (M["m00"] == 0): M["m00"] = 1

                x = int(M["m10"]/M["m00"])
                y = int(M["m01"]/M["m00"])
                font = cv.FONT_HERSHEY_SIMPLEX

                cv.circle(video, (x, y), 5, (255,255,255), -1)
                cv.putText(video, text, (x, y+200), font, 1, (0,0,0), 5, cv.LINE_AA)
                contorno_suavisado = cv.convexHull(c)
                cv.drawContours(video ,[contorno_suavisado], 0 , (0,0,0) , 10)
                