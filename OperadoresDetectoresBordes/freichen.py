import cv2
import math
import numpy as np

path = 'Resources/7228837.jpg'

img = cv2.imread(path, 0)

img = np.float32(img)

h, w = img.shape[:2]

fr0 = np.zeros((h, w))
fr1 = np.zeros((h, w))
fr2 = np.zeros((h, w))
fr3 = np.zeros((h, w))
fr4 = np.zeros((h, w))


for row in range(h-1):
    for col in range(w-1):
        fr0[row][col] = (np.divide(1, 2*math.sqrt(2))) * (+ 1 * img[row - 1][col - 1] + math.sqrt(2) * img[row - 1][col] + 1 * img[row - 1][col + 1]
                        + 0 * img[row][col-1] + 0 * img[row][col] + 0 * img[row][col+1]
                        - 1 * img[row+1][col-1] - math.sqrt(2) * img[row+1][col] - 1 * img[row+1][col+1])

        fr1[row][col] = (np.divide(1, 2*math.sqrt(2))) * (+ 1 * img[row - 1][col - 1] + 0 * img[row - 1][col] - 1 * img[row - 1][col + 1]
                        + math.sqrt(2) * img[row][col-1] + 0 * img[row][col] - math.sqrt(2) * img[row][col+1]
                        + 1 * img[row+1][col-1] - 0 * img[row+1][col] - 1 * img[row+1][col+1])

        fr2[row][col] = (np.divide(1, 2*math.sqrt(2))) * (+ 0 * img[row - 1][col - 1] - 1 * img[row - 1][col] - math.sqrt(2) * img[row - 1][col + 1]
                        + 1 * img[row][col-1] + 0 * img[row][col] - 1 * img[row][col+1]
                        - math.sqrt(2) * img[row+1][col-1] + 1 * img[row+1][col] + 0 * img[row+1][col+1])

        fr3[row][col] = (np.divide(1, 2*math.sqrt(2))) * (+ math.sqrt(2) * img[row - 1][col - 1] - 1 * img[row - 1][col] + 0 * img[row - 1][col + 1]
                        - 1 * img[row][col-1] + 0 * img[row][col] + 1 * img[row][col+1]
                        + 0 * img[row+1][col-1] + 1 * img[row+1][col] - math.sqrt(2) * img[row+1][col+1])

        fr4[row][col] = np.divide(1, 2) * (+ 0 * img[row - 1][col - 1] + 1 * img[row - 1][col] + 0 * img[row - 1][col + 1]
                        - 1 * img[row][col-1] + 0 * img[row][col] - 1 * img[row][col+1]
                        + 0 * img[row+1][col-1] + 1 * img[row+1][col] + 0 * img[row+1][col+1])

        if fr0[row][col] < 0:
            fr0[row][col] = 0
        if fr1[row][col] < 0:
            fr1[row][col] = 0
        if fr2[row][col] < 0:
            fr2[row][col] = 0
        if fr3[row][col] < 0:
            fr3[row][col] = 0
        if fr4[row][col] < 0:
            fr4[row][col] = 0


fr0 = np.uint8(fr0)
fr1 = np.uint8(fr1)
fr2 = np.uint8(fr2)
fr3 = np.uint8(fr3)
fr4 = np.uint8(fr4)


cv2.imshow("Frei-chen 0", fr0)
cv2.imshow("Frei-chen 45", fr1)
cv2.imshow("Frei-chen 90", fr2)
cv2.imshow("Frei-chen 135", fr3)
cv2.imshow("Frei-chen 180", fr4)
cv2.waitKey(0)
cv2.destroyAllWindows()