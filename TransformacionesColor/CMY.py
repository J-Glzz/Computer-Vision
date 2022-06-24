import cv2
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path)

B = img[:, :, 0] / 255
G = img[:, :, 1] / 255
R = img[:, :, 2] / 255

CMY = [(1-B), (1-G), (1-R)]

result = cv2.merge(CMY)

cv2.imshow("CMY", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
