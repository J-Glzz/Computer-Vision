import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)
img = np.float32(img)

B, G, R = cv2.split(img)

alfa = 1

B = (np.divide(255, 1-np.exp(-alfa)))*(1-np.exp(np.divide(-alfa*B, 255)))
G = (np.divide(255, 1 - np.exp(-alfa))) * (1 - np.exp(np.divide(-alfa*G, 255)))
R = (np.divide(255, 1-np.exp(-alfa)))*(1-np.exp(np.divide(-alfa*R, 255)))

expo = cv2.merge([B, G, R]).astype(np.uint8)

grises = (R*0.114 + G*0.587 + B*0.229).astype(np.uint8)

cv2.imshow("Función Exponencial", grises)
cv2.waitKey(0)
cv2.destroyAllWindows()