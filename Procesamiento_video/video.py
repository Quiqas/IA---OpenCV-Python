import numpy as np
import cv2 as cv

#Objeto de captura de video.

cap = cv.VideoCapture(0)

#Objeto de guardado de video

fourcc = cv.cv.CV_FOURCC(*'XVID')
out = cv.VideoWriter('Yo.avi', fourcc, 20.0, (640,480))
while(True):
	#Captura cuadro por cuadro
	ret, frame = cap.read()
	
	if ret==True:
		frame = cv.flip(frame,0)
		
		out.write(frame)
		#Las operaciones sobre aqui
		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		
		#Muestra el resultado
		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

#Cuando termina, libera el video
cap.release()
out.release()
cv.destroyAllWindows()
