import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

isotropicoX = np.zeros((h, w))
isotropicoY = np.zeros((h, w))

kx = np.array([[-1, 0, 1], [-(math.sqrt(2)), 0, (math.sqrt(2))], [-1, 0, 1]], dtype=int)
ky = np.array([[-1, -(math.sqrt(2)), -1], [0, 0, 0], [1, (math.sqrt(2)), 1]], dtype=int)

for row in range(h-1):
    for col in range(w-1):
        isotropicoX[row][col] = - 1 * img[row - 1][col - 1] + 0 * img[row - 1][col] + 1 * img[row - 1][col + 1] \
                                - (math.sqrt(2)) * img[row][col-1] + 0 * img[row][col] + (math.sqrt(2)) * img[row][col+1] \
                                - 1 * img[row+1][col-1] + 0 * img[row+1][col] + 1 * img[row+1][col+1]
        if isotropicoX[row][col] < 0:
            isotropicoX[row][col] = 0


for row in range(h-1):
    for col in range(w-1):
        isotropicoY[row][col] = - 1 * img[row - 1][col - 1] - (math.sqrt(2)) * img[row - 1][col] - 1 * img[row - 1][col + 1] \
                                + 0 * img[row][col-1] + 0 * img[row][col] + 0 * img[row][col+1] \
                                + 1 * img[row+1][col-1] + (math.sqrt(2)) * img[row+1][col] + 1 * img[row+1][col+1]
        if isotropicoY[row][col] < 0:
            isotropicoY[row][col] = 0


isotropicoX = np.uint8(isotropicoX)
isotropicoY = np.uint8(isotropicoY)

isotropico = cv2.add(isotropicoX, isotropicoY)

funx = cv2.filter2D(img, ddepth=-1, kernel=kx)
funy = cv2.filter2D(img, ddepth=-1, kernel=ky)
funx = cv2.convertScaleAbs(funx)
funy = cv2.convertScaleAbs(funy)
fun = cv2.add(funx, funy)

cv2.imshow("Isotropico X", isotropicoX)
cv2.imshow("Isotropico Y", isotropicoY)
cv2.imshow("Isotropico", isotropico)
cv2.imshow("Funcion", fun)
cv2.waitKey(0)
cv2.destroyAllWindows()