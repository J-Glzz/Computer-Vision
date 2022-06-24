import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

kirsch0= np.zeros((h, w))
kirsch45 = np.zeros((h, w))
kirsch90 = np.zeros((h, w))
kirsch135 = np.zeros((h, w))
kirsch180 = np.zeros((h, w))
kirsch225 = np.zeros((h, w))
kirsch270 = np.zeros((h, w))
kirsch315 = np.zeros((h, w))


for row in range(h-1):
    for col in range(w-1):
        kirsch0[row][col] = - 3 * img[row-1][col-1] - 3 * img[row-1][col] + 5 * img[row-1][col+1] \
                            - 3 * img[row][col-1] + 0 * img[row][col] + 5 * img[row][col+1] \
                            - 3 * img[row+1][col-1] - 3 * img[row+1][col] + 5 * img[row+1][col+1]

        kirsch45[row][col] = - 3 * img[row-1][col-1] + 5 * img[row-1][col] + 5 * img[row-1][col+1] \
                             - 3 * img[row][col-1] + 0 * img[row][col] + 5 * img[row][col+1] \
                             - 3 * img[row+1][col-1] - 3 * img[row+1][col] - 3 * img[row+1][col+1]

        kirsch90[row][col] = + 5 * img[row-1][col-1] + 5 * img[row-1][col] + 5 * img[row-1][col+1] \
                             - 3 * img[row][col-1] + 0 * img[row][col] - 3 * img[row][col+1] \
                             - 3 * img[row+1][col-1] - 3 * img[row+1][col] - 3 * img[row+1][col+1]

        kirsch135[row][col] = + 5 * img[row-1][col-1] + 5 * img[row-1][col] - 3 * img[row-1][col+1] \
                              + 5 * img[row][col-1] + 0 * img[row][col] - 3 * img[row][col+1] \
                              - 3 * img[row+1][col-1] - 3 * img[row+1][col] - 3 * img[row+1][col+1]

        kirsch180[row][col] = + 5 * img[row-1][col-1] - 3 * img[row-1][col] - 3 * img[row-1][col+1] \
                              + 5 * img[row][col-1] + 0 * img[row][col] - 3 * img[row][col+1] \
                              + 5 * img[row+1][col-1] - 3 * img[row+1][col] - 3 * img[row+1][col+1]

        kirsch225[row][col] = - 3 * img[row-1][col-1] - 3 * img[row-1][col] - 3 * img[row-1][col+1] \
                              + 5 * img[row][col-1] + 0 * img[row][col] - 3 * img[row][col+1] \
                              + 5 * img[row+1][col-1] + 5 * img[row+1][col] - 3 * img[row+1][col+1]

        kirsch270[row][col] = - 3 * img[row-1][col-1] - 3 * img[row-1][col] - 3 * img[row-1][col+1] \
                              - 3 * img[row][col-1] + 0 * img[row][col] - 3 * img[row][col+1] \
                              + 5 * img[row+1][col-1] + 5 * img[row+1][col] + 5 * img[row+1][col+1]

        kirsch315[row][col] = - 3 * img[row-1][col-1] - 3 * img[row-1][col] - 3 * img[row-1][col+1] \
                              - 3 * img[row][col-1] + 0 * img[row][col] + 5 * img[row][col+1] \
                              - 3 * img[row+1][col-1] + 5 * img[row+1][col] + 5 * img[row+1][col+1]

        if kirsch0[row][col] < 0:
            kirsch0[row][col] = 0
        if kirsch45[row][col] < 0:
            kirsch45[row][col] = 0
        if kirsch90[row][col] < 0:
            kirsch90[row][col] = 0
        if kirsch135[row][col] < 0:
            kirsch135[row][col] = 0
        if kirsch180[row][col] < 0:
            kirsch180[row][col] = 0
        if kirsch225[row][col] < 0:
            kirsch225[row][col] = 0
        if kirsch270[row][col] < 0:
            kirsch270[row][col] = 0
        if kirsch315[row][col] < 0:
            kirsch315[row][col] = 0


kirsch0 = np.uint8(kirsch0)
kirsch45 = np.uint8(kirsch45)
kirsch90 = np.uint8(kirsch90)
kirsch135 = np.uint8(kirsch135)
kirsch180 = np.uint8(kirsch180)
kirsch225 = np.uint8(kirsch225)
kirsch270 = np.uint8(kirsch270)
kirsch315 = np.uint8(kirsch315)

cv2.imshow("Kirsch 0", kirsch0)
cv2.imshow("Kirsch 45", kirsch45)
cv2.imshow("Kirsch 90", kirsch90)
cv2.imshow("Kirsch 135", kirsch135)
cv2.imshow("Kirsch 180", kirsch180)
cv2.imshow("Kirsch 225", kirsch225)
cv2.imshow("Kirsch 270", kirsch270)
cv2.imshow("Kirsch 315", kirsch315)
cv2.waitKey(0)
cv2.destroyAllWindows()