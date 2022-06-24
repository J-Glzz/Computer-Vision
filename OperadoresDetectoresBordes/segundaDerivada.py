import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[0:2]

SderivadaX = np.zeros((w, h))
SderivadaY = np.zeros((w, h))

kernel = np.array([1, -2, 1], dtype=int)

for row in range(h-1):
    for col in range(w-1):
        SderivadaX[row][col] = img[row - 1, col] - 2 * img[row, col] + img[row + 1, col]
        if (SderivadaX[row][col] < 0):
            SderivadaX[row][col] = 0


for row in range(h-1):
    for col in range(w-1):
        SderivadaY[row][col] = img[row, col - 1] - 2 * img[row, col] + img[row, col + 1]
        if (SderivadaY[row][col] < 0):
            SderivadaY[row][col] = 0

SderivadaX = np.uint8(SderivadaX)
SderivadaY = np.uint8(SderivadaY)

suma = SderivadaX + SderivadaY

deri = cv2.filter2D(img, ddepth=-1, kernel=kernel)

deri = cv2.convertScaleAbs(deri)


cv2.imshow("Resultado en X", SderivadaX)
cv2.imshow("Resultado en Y", SderivadaY)
cv2.waitKey(0)
cv2.destroyAllWindows()