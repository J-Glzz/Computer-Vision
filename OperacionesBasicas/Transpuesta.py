import cv2
import numpy as np

path1 = 'Resources/7ad8dba8bc19831d047eb0ebed4eea5c.jpg'

img = cv2.imread(path1)

imgArr = np.array(img, dtype='int').tolist()

matrizImg = imgArr
ancho = len(matrizImg[0])
alto = len(matrizImg)
mTranspuesta = []
for row in range(ancho):
    filas = []
    for col in range(alto):
       filas.append(matrizImg[col][row])
    mTranspuesta.append(filas)


cv2.imshow('Original - Transpuesta', cv2.hconcat([img, np.uint8(mTranspuesta)]) )
cv2.waitKey(0)
cv2.destroyAllWindows()