# 2.4Lineas_y_rectangulos
Es la cuarta tarea del Segundo Parcial de mi materia de Análisis y Procesamiento de Imágenes

## *INSTRUCCIONES*
Entregar: 
- el dibujo adjunto en JPG, elaborado con opencv. 
- el programa utilizado en PY.


```
import cv2
import numpy as np
imagen = 255*np.ones((400,600,3),dtype=np.uint8)
#                      f   c  d
#linea azul BGR
cv2.line(imagen,(0,0),(600,400),(255,0,0),1)
#                       x   y    
#rectangulo           x   y
cv2.rectangle(imagen,(10,10),(100,200),(0,255,0),2)
#                    psi pid
#circulo
cv2.circle(imagen,(300,200),200,(0,0,255),4)
#texto
font = 0#01234567
cv2.putText(imagen,'Salvador',(300,200),font,1,(145,200,20),2,cv2.LINE_AA)

cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows
```
