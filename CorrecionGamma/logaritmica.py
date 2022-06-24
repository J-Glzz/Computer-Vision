import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)
img = np.float32(img)

B, G, R = cv2.split(img)

alfa = 1

B = (255/np.log(alfa*255+1))*np.log(alfa*B+1)
G = (255/np.log(alfa*255+1))*np.log(alfa*G+1)
R = (255/np.log(alfa*255+1))*np.log(alfa*R+1)

log = cv2.merge([B, G, R]).astype(np.uint8)

grises = (R*0.114 + G*0.587 + B*0.229).astype(np.uint8)

cv2.imshow("Función logarítmica", grises)
cv2.waitKey(0)
cv2.destroyAllWindows()