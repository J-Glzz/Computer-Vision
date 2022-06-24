import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

sobelX = np.zeros((h, w))
sobelY = np.zeros((h, w))

kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=int)
ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=int)

for row in range(h-1):
    for col in range(w-1):
        sobelX[row][col] = - 1 * img[row-1][col-1] + 0 * img[row-1][col] + 1 * img[row-1][col+1] \
                           - 2 * img[row][col-1] + 0 * img[row][col] + 2 * img[row][col+1] \
                           - 1 * img[row+1][col-1] + 0 * img[row+1][col] + 1 * img[row+1][col+1]
        if sobelX[row][col] < 0:
            sobelX[row][col] = 0


for row in range(h-1):
    for col in range(w-1):
        sobelY[row][col] = - 1 * img[row-1][col-1] - 2 * img[row-1][col] - 1 * img[row-1][col+1] \
                           + 0 * img[row][col-1] + 0 * img[row][col] + 0 * img[row][col+1] \
                           + 1 * img[row+1][col-1] + 2 * img[row+1][col] + 1 * img[row+1][col+1]
        if sobelY[row][col] < 0:
            sobelY[row][col] = 0


sobelX = np.uint8(sobelX)
sobelY = np.uint8(sobelY)

sobel = cv2.add(sobelX, sobelY)

funx = cv2.filter2D(img, ddepth=-1, kernel=kx)
funy = cv2.filter2D(img, ddepth=-1, kernel=ky)
funx = cv2.convertScaleAbs(funx)
funy = cv2.convertScaleAbs(funy)
fun = cv2.add(funx, funy)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel", sobel)
cv2.imshow("Funcion", fun)
cv2.waitKey(0)
cv2.destroyAllWindows()