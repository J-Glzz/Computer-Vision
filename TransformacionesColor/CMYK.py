import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)

B = img[:, :, 0] / 255
G = img[:, :, 1] / 255
R = img[:, :, 2] / 255


K = 1 - np.maximum(np.maximum(R, G), B)

CMYK = [(1-B-K)/(1-K), (1-G-K)/(1-K), (1-R-K)/(1-K)]

result = cv2.merge(CMYK)

cv2.imshow("CMYK", result)
cv2.waitKey(0)