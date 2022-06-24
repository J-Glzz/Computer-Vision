import cv2
import math
import numpy as np


errorState = np.errstate(divide='ignore', invalid='ignore')

def RGB2HSV(img):

    with errorState:
        IMG = np.float32(img)

        B, G, R = cv2.split(IMG)

        def cal_H(R, B, G):
            H = np.copy(G)

            for i in range(0, B.shape[0]):
                for j in range(0, B.shape[1]):
                    H[i][j] = 0.5 * ((R[i][j] - G[i][j]) + (R[i][j] - B[i][j])) / math.sqrt((R[i][j] - G[i][j]) ** 2 + ((R[i][j] - B[i][j]) * (G[i][j] - B[i][j])))
                    H[i][j] = math.acos(H[i][j])

                    if B[i][j] <= G[i][j]:
                        H[i][j] = H[i][j]
                    else:
                        H[i][j] = ((360 * math.pi) / 180.0) - H[i][j]

            return H

        def cal_S(R, B, G):
            min = np.minimum(np.minimum(R, G), B)
            max = np.maximum(np.maximum(R, B), B)
            S = np.divide((max - min), max)
            return S

        def cal_V(R, B, G):
            max = np.maximum(np.maximum(R, G), B)
            V = np.divide(max, 255)
            return V



        HSV = cv2.merge((cal_H(R, B, G), cal_S(R, B, G), cal_V(R, B, G)))
        cv2.imshow("HSV", HSV)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


path = 'Resources/7228837.jpg'
img = cv2.imread(path)
RGB2HSV(img)