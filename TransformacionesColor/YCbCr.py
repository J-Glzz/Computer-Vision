import cv2
import numpy as np

path = 'Resources/7228837.jpg'
img = cv2.imread(path)

YCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow("YCbCr", YCbCr)
cv2.waitKey(0)
cv2.destroyAllWindows()