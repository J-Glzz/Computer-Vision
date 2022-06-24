import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

B = np.zeros((h, w))

P1 = 50
P2 = 150

for row in range(h-1):
    for col in range(w-1):
        B[row][col] = img[row][col]
        if img[row][col] < P1 or img[row][col] >= P2:
            B[row][col] = 255
        else:
            B[row][col] = 0


B = np.uint8(B)

cv2.imshow("Umbral Binario", B)
cv2.waitKey(0)
cv2.destroyAllWindows()