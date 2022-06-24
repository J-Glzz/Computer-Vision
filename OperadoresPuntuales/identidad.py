import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

B = np.zeros((h, w))

for row in range(h-1):
    for col in range(w-1):
        B[row][col] = img[row][col]

B = np.uint8(B)

cv2.imshow("Identidad", B)
cv2.waitKey(0)
cv2.destroyAllWindows()