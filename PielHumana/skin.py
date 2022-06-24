import cv2
import numpy as np

path = 'Resources/enfermedades-de-la-piel.jpg'

img = cv2.imread(path)

img = cv2.resize(img, (377, 377))

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

channelV = imgHSV[:, :, 2]

h, w = channelV.shape

morfo = cv2.morphologyEx(channelV, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))

morfo_result = cv2.bitwise_not(morfo)

adap = cv2.adaptiveThreshold(morfo_result, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, -1)

res = cv2.bitwise_or(adap, morfo_result)

copia = np.zeros((h, w))

P1 = 100
P2 = 255

for row in range(h-1):
    for col in range(w-1):
        copia[row][col] = res[row][col]
        if res[row][col] < P1 or res[row][col] >= P2:
            copia[row][col] = 255
        else:
            copia[row][col] = 0


copia = np.uint8(copia)


cv2.imshow("original", img)
cv2.imshow("CanalV", channelV)
cv2.imshow("expansion", morfo)
cv2.imshow("resultado", copia)
cv2.waitKey(0)
cv2.destroyAllWindows()