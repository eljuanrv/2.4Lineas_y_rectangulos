import cv2
import numpy as np
imagen = 220*np.ones((700,700,3),dtype=np.uint8)
#                      f   c  d

#rectangulo           x    y                rojo
cv2.rectangle(imagen,(250,250),(450,450),(0,0,255),4)
#                       psi        pid

#circulo central
cv2.circle(imagen,(350,350),100,(0,0,255),4)

#circulo superior izquierdo
cv2.circle(imagen,(250,250),100,(199,152,39),4)
#circulo superior derecho
cv2.circle(imagen,(450,250),100,(79,168,45),4)
#circulo inferior derecho
cv2.circle(imagen,(450,450),100,(199,152,39),4)
#circulo inferior izquierdo
cv2.circle(imagen,(250,450),100,(79,168,45),4)

#texto
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(imagen,'Juan',(315,357),font,1,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows