import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

prewittX = np.zeros((h, w))
prewittY = np.zeros((h, w))

kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=int)

for row in range(h-1):
    for col in range(w-1):
        prewittX[row][col] = - (1 * img[row-1][col-1]) + (0 * img[row-1][col]) + (1 * img[row-1][col+1]) \
                             - (1 * img[row][col-1]) + (0 * img[row][col]) + (1 * img[row][col+1]) \
                             - (1 * img[row+1][col-1]) + (0 * img[row+1][col]) + (1 * img[row+1][col+1])

        if prewittX[row][col] < 0:
            prewittX[row][col] = 0

for row in range(h-1):
    for col in range(w-1):
        prewittY[row][col] = - (1 * img[row-1][col-1]) - (1 * img[row-1][col]) - (1 * img[row-1][col+1]) \
                             + (0 * img[row][col-1]) + (0 * img[row][col]) + (0 * img[row][col+1]) \
                             + (1 * img[row+1][col-1]) + (1 * img[row+1][col]) + (1 * img[row+1][col+1])

        if prewittY[row][col] < 0:
            prewittY[row][col] = 0


prewittX = np.uint8(prewittX)
prewittY = np.uint8(prewittY)

prewitt = cv2.add(prewittX, prewittY)

funx = cv2.filter2D(img, ddepth=-1, kernel=kx)
funy = cv2.filter2D(img, ddepth=-1, kernel=ky)
funx = cv2.convertScaleAbs(funx)
funy = cv2.convertScaleAbs(funy)
fun = cv2.add(funx, funy)

cv2.imshow("Prewitt en X", prewittX)
cv2.imshow("Prewitt en Y", prewittY)
cv2.imshow("Prewitt", prewitt)
cv2.imshow("Funcion", fun)
cv2.waitKey(0)
cv2.destroyAllWindows()