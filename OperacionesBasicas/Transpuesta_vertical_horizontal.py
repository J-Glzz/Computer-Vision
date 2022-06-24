import cv2
import numpy as np

path1 = 'Resources/7ad8dba8bc19831d047eb0ebed4eea5c.jpg'

img = cv2.imread(path1)

imgArr = np.array(img, dtype='int').tolist()

matrizImg = imgArr
ancho = len(matrizImg[0])
alto = len(matrizImg)
for y in range(alto):
    for x in range(int(ancho/2)):
        reflejo = ancho - x - 1
        opuesto = matrizImg[y][reflejo]
        original = matrizImg[y][x]
        matrizImg[y][reflejo] = original
        matrizImg[y][x] = opuesto


cv2.imshow('Horizontal', np.uint8(matrizImg))
cv2.waitKey(0)
cv2.destroyAllWindows()