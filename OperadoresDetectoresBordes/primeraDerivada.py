import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[0:2]

derivadaX = np.zeros((w, h))
derivadaY = np.zeros((w, h))

for row in range(h-1):
    for col in range(w-1):
        derivadaX[row][col] = img[row-1, col]-img[row, col]
        if derivadaX[row][col] < 0:
            derivadaX[row][col] = 0


for row in range(h-1):
    for col in range(w-1):
        derivadaY[row][col] = img[row, col-1] - img[row, col]
        if derivadaY[row][col] < 0:
            derivadaY[row][col] = 0

derivadaX = np.uint8(derivadaX)
derivadaY = np.uint8(derivadaY)

cv2.imshow("Resultado X", derivadaX)
cv2.imshow("Resultado Y", derivadaY)
cv2.waitKey(0)
cv2.destroyAllWindows()