import cv2
import numpy as np
import math

errorState = np.errstate(divide='ignore', invalid='ignore')

def RGB2HSI(img):

    with errorState:
        IMG = np.float32(img) / 255

        B, G, R = cv2.split(IMG)

        def cal_H(R, B, G):
            H = np.copy(R)

            for i in range(0, B.shape[0]):
                for j in range(0, B.shape[1]):
                    H[i][j] = 0.5 * ((R[i][j] - G[i][j]) + (R[i][j] - B[i][j])) / \
                              math.sqrt((R[i][j] - G[i][j]) ** 2 +
                                          ((R[i][j] - B[i][j]) * (G[i][j] - B[i][j])))
                    H[i][j] = math.acos(H[i][j])

                    if B[i][j] <= G[i][j]:
                        H[i][j] = H[i][j]
                    else:
                        H[i][j] = ((360 * math.pi) / 180.0) - H[i][j]

            return H

        def cal_S(R, B, G):
            min = np.minimum(np.minimum(R, G), B)
            S = 1 - (3 / (R + G + B + 0.001) * min)

            return S

        def cal_I(R, B, G):
            return np.divide(B + G + R, 3)


        hsi = cv2.merge((cal_H(R, B, G), cal_S(R, B, G), cal_I(R, B, G)))
        cv2.imshow("HSI", hsi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


path = 'Resources/7228837.jpg'
img = cv2.imread(path)
RGB2HSI(img)