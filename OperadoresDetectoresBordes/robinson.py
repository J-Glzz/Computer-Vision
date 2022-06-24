import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

robinson0 = np.zeros((h, w))
robinson45 = np.zeros((h, w))
robinson90 = np.zeros((h, w))
robinson135 = np.zeros((h, w))
robinson180 = np.zeros((h, w))
robinson225 = np.zeros((h, w))
robinson270 = np.zeros((h, w))
robinson315 = np.zeros((h, w))


for row in range(h-1):
    for col in range(w-1):
        robinson0[row][col] = - 1 * img[row-1][col-1] + 0 * img[row-1][col] + 1 * img[row-1][col+1] \
                              - 2 * img[row][col-1] + 0 * img[row][col] + 2 * img[row][col+1] \
                              - 1 * img[row+1][col-1] + 0 * img[row+1][col] + 1 * img[row+1][col+1]

        robinson45[row][col] = + 0 * img[row-1][col-1] + 1 * img[row-1][col] + 2 * img[row-1][col+1] \
                               - 1 * img[row][col-1] + 0 * img[row][col] + 1 * img[row][col+1] \
                               - 2 * img[row+1][col-1] - 1 * img[row+1][col] + 0 * img[row+1][col+1]

        robinson90[row][col] = + 1 * img[row-1][col-1] + 2 * img[row-1][col] + 1 * img[row-1][col+1] \
                               + 0 * img[row][col-1] + 0 * img[row][col] + 0 * img[row][col+1] \
                               - 1 * img[row+1][col-1] - 2 * img[row+1][col] - 1 * img[row+1][col+1]

        robinson135[row][col] = + 2 * img[row-1][col-1] + 1 * img[row-1][col] + 0 * img[row-1][col+1] \
                                + 1 * img[row][col-1] + 0 * img[row][col] - 1 * img[row][col+1] \
                                + 0 * img[row+1][col-1] - 1 * img[row+1][col] - 2 * img[row+1][col+1]

        robinson180[row][col] = + 1 * img[row-1][col-1] + 0 * img[row-1][col] - 1 * img[row-1][col+1] \
                                + 2 * img[row][col-1] + 0 * img[row][col] - 2 * img[row][col+1] \
                                + 1 * img[row+1][col-1] + 0 * img[row+1][col] - 1 * img[row+1][col+1]

        robinson225[row][col] = + 0 * img[row-1][col-1] - 1 * img[row-1][col] - 2 * img[row-1][col+1] \
                                + 1 * img[row][col-1] + 0 * img[row][col] - 1 * img[row][col+1] \
                                + 2 * img[row+1][col-1] + 1 * img[row+1][col] + 0 * img[row+1][col+1]

        robinson270[row][col] = - 1 * img[row-1][col-1] - 2 * img[row-1][col] - 1 * img[row-1][col+1] \
                                + 0 * img[row][col-1] + 0 * img[row][col] + 0 * img[row][col+1] \
                                + 1 * img[row+1][col-1] + 2 * img[row+1][col] + 1 * img[row+1][col+1]

        robinson315[row][col] = - 2 * img[row-1][col-1] - 1 * img[row-1][col] + 0 * img[row-1][col+1] \
                                - 1 * img[row][col-1] + 0 * img[row][col] + 1 * img[row][col+1] \
                                + 0 * img[row+1][col-1] + 1 * img[row+1][col] + 2 * img[row+1][col+1]

        if robinson0[row][col] < 0:
            robinson0[row][col] = 0
        if robinson45[row][col] < 0:
            robinson45[row][col] = 0
        if robinson90[row][col] < 0:
            robinson90[row][col] = 0
        if robinson135[row][col] < 0:
            robinson135[row][col] = 0
        if robinson180[row][col] < 0:
            robinson180[row][col] = 0
        if robinson225[row][col] < 0:
            robinson225[row][col] = 0
        if robinson270[row][col] < 0:
            robinson270[row][col] = 0
        if robinson315[row][col] < 0:
            robinson315[row][col] = 0


robinson0 = np.uint8(robinson0)
robinson45 = np.uint8(robinson45)
robinson90 = np.uint8(robinson90)
robinson135 = np.uint8(robinson135)
robinson180 = np.uint8(robinson180)
robinson225 = np.uint8(robinson225)
robinson270 = np.uint8(robinson270)
robinson315 = np.uint8(robinson315)

cv2.imshow("Robinson 0", robinson0)
cv2.imshow("Robinson 45", robinson45)
cv2.imshow("Robinson 90", robinson90)
cv2.imshow("Robinson 135", robinson135)
cv2.imshow("Robinson 180", robinson180)
cv2.imshow("Robinson 225", robinson225)
cv2.imshow("Robinson 270", robinson270)
cv2.imshow("Robinson 315", robinson315)
cv2.waitKey(0)
cv2.destroyAllWindows()