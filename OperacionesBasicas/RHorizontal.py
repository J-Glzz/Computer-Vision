import cv2
import numpy as np

path1 = 'Resources/7ad8dba8bc19831d047eb0ebed4eea5c.jpg'

img = cv2.imread(path1)

imgArr = np.array(img, dtype='int').tolist()

matrizImg = imgArr
ancho = len(matrizImg[0])
alto = len(matrizImg)
for col in range(alto):
    for row in range(int(ancho/2)):
        reflejo = ancho - row - 1
        opuesto = matrizImg[col][reflejo]
        original = matrizImg[col][row]
        matrizImg[col][reflejo] = original
        matrizImg[col][row] = opuesto


cv2.imshow('Original - Horizontal', cv2.hconcat([img, np.uint8(matrizImg)]) )
cv2.waitKey(0)
cv2.destroyAllWindows()