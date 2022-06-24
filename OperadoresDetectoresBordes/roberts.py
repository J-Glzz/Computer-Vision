import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

robertsX = np.zeros((h, w))
robertsY = np.zeros((h, w))

kx = np.array([[0, 1], [-1, 0]], dtype=int)
ky = np.array([[1, 0], [0, -1]], dtype=int)

for row in range(h-1):
    for col in range(w-1):
        robertsX[row][col] = 0 * img[row-1][col-1] + 1 * img[row-1][col] \
                             - 1 * img[row][col-1] + 0 * img[row][col]
        if robertsX[row][col] < 0:
            robertsX[row][col] = 0


for row in range(h-1):
    for col in range(w-1):
        robertsY[row][col] = 1 * img[row-1][col-1] + 0 * img[row-1][col] \
                             + 0 * img[row][col-1] - 1 * img[row][col]
        if robertsY[row][col] < 0:
            robertsY[row][col] = 0


robertsX = np.uint8(robertsX)
robertsY = np.uint8(robertsY)

roberts = cv2.add(robertsX, robertsY)

funx = cv2.filter2D(img, ddepth=-1, kernel=kx)
funy = cv2.filter2D(img, ddepth=-1, kernel=ky)
funx = cv2.convertScaleAbs(funx)
funy = cv2.convertScaleAbs(funy)
fun = cv2.add(funx, funy)

cv2.imshow("Roberts X", robertsX)
cv2.imshow("Roberts Y", robertsY)
cv2.imshow("Roberts", roberts)
cv2.imshow("Funcion", fun)
cv2.waitKey(0)
cv2.destroyAllWindows()