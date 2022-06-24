import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)
img = np.float32(img)

B, G, R = cv2.split(img)

B = 255 * (1-np.cos(np.divide(math.pi*B, 2*255)))
G = 255 * (1-np.cos(np.divide(math.pi*G, 2*255)))
R = 255 * (1-np.cos(np.divide(math.pi*R, 2*255)))

coseno = cv2.merge([B, G, R]).astype(np.uint8)

grises = (R*0.114 + G*0.587 + B*0.229).astype(np.uint8)

cv2.imshow("Función Cosenoidal", grises)
cv2.waitKey(0)
cv2.destroyAllWindows()