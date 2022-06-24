import cv2
import numpy as np
import math

path1 = 'Resources/7ad8dba8bc19831d047eb0ebed4eea5c.jpg'
path2 = 'Resources/7228837.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# Se convierten las imagenes a float
img1 = img1 / 1
img2 = img2 / 1

Suma = ((img1) + (img2))/2

Resta = abs((img1 - img2)/2)

Multi = (img1 * img2)/255

Suma = np.uint8(Suma)
Resta = np.uint8(Resta)
Multi = np.uint8(Multi)

cv2.imshow('Suma', Suma)
cv2.imshow('Resta', Resta)
cv2.imshow('Multiplicacion', Multi)
cv2.waitKey(0)
cv2.destroyAllWindows()