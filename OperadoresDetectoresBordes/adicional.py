import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

adi = np.zeros((h, w))


for row in range(h-1):
    for col in range(w-1):
        adi[row][col] = + 0 * img[row-1][col-1] + 1 * img[row-1][col] + 0 * img[row-1][col+1] \
                        + 1 * img[row][col-1] - 4 * img[row][col] + 1 * img[row][col+1] \
                        + 0 * img[row+1][col-1] + 1 * img[row+1][col] + 0 * img[row+1][col+1]

        if adi[row][col] < 0:
            adi[row][col] = 0

adi = np.uint8(adi)

cv2.imshow("Adicional", adi)
cv2.waitKey(0)
cv2.destroyAllWindows()