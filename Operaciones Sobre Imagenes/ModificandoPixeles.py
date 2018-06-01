import numpy as np
import cv2 as cv

img = cv.imread('One.png')


#Devuelve la cantidad de filas, columnas y canales (En caso de ser a color)
print( img.shape)


#En esta estructura c1 es la columna con el pixelque se desea seleccionar empezando por la izquierda
#y c es el pixel final, lo mismo se aplica para r1 y r pero estas siendo filas
#ROI = img[c1: c, r1:r]
#O mas sencillo img[Largo , Ancho]
ROI = img[370:680, 910:1165]

img[490: 800, 200: 455] = ROI

img[:,7,:] = 0


cv.imwrite('One Piece Photo ROI.png', img)


cv.waitKey(0)
cv.destroyAllWindows()
