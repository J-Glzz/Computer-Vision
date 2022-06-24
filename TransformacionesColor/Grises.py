import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

grises = (R*0.114 + G*0.587 + B*0.229).astype(np.uint8)


cv2.imshow('Imagen', grises)
cv2.waitKey(0)
cv2.destroyAllWindows()
