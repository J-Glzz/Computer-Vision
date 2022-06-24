import cv2
import numpy as np

path1 = 'Resources/7ad8dba8bc19831d047eb0ebed4eea5c.jpg'

img = cv2.imread(path1)

imgArr = np.array(img, dtype='int').tolist()

matrizImg = imgArr
ancho = len(matrizImg[0])
alto = len(matrizImg)
for row in range(ancho):
    for col in range(int(alto/2)):
        reflejo = alto - col - 1
        opuesto = matrizImg[reflejo][row]
        original = matrizImg[col][row]
        matrizImg[reflejo][row] = original
        matrizImg[col][row] = opuesto


cv2.imshow('Original - Vertical', cv2.hconcat([img, np.uint8(matrizImg)]))
cv2.waitKey(0)
cv2.destroyAllWindows()