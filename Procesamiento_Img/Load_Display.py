import numpy as np
import cv2 as cv

#Carga una imagen a color en escala de grises 

img = cv.imread('One.png',0);

#Muestra la imagen en una ventana

cv.imshow('One Piece Photo', img)

cv.imwrite('OnePieceCopy.png', img)
cv.waitKey(0)
cv.destroyAllWindows()
