import cv2

path = 'Resources/7228837.jpg'
img = cv2.imread(path)
canales = img.copy()

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canales")
input("Presiona una tecla para continuar...")
canales = img.copy()
B = canales[:, :, 0]
G = canales[:, :, 1]
R = canales[:, :, 2]
cv2.imshow("Canal R", R)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canal B")
input("Presiona una tecla para continuar...")
canalB = img.copy()
canalB[:, :, 0]
canalB[:, :, 1] = 0
canalB[:, :, 2] = 0
cv2.imshow("Canal B", canalB)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canal G")
input("Presiona una tecla para continuar...")
canalG = img.copy()
canalG[:, :, 0] = 0
canalG[:, :, 1]
canalG[:, :, 2] = 0
cv2.imshow("Canal G", canalG)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canal R")
input("Presiona una tecla para continuar...")
canalR = img.copy()
canalR[:, :, 0] = 0
canalR[:, :, 1] = 0
canalR[:, :, 2]
cv2.imshow("Canal R", canalR)
cv2.waitKey(0)
cv2.destroyAllWindows()