import cv2
import numpy as np

path = 'chicles/Pepto1-5.jpeg'
# Lectura de la imagen
img = cv2.imread(path)
# Reescalado de la imagen original
rees = cv2.resize(img, (720, 720))
# Separación de canales
B, G, R = cv2.split(rees)
# Conversión de espacio de color RGB a escala de grises
grises = (R*0.114 + G*0.587 + B*0.229).astype(np.uint8)
# Ecualización de histograma a la imagen en escala de grises
histo = cv2.equalizeHist(grises, cv2.CV_64F)
# Copia de la imagen ecualizada
nueva = histo.copy()
# Conversión a float para poder operar con la imagen
nueva = np.float_(nueva)
# Obtención de dimensiones de la imagen nueva
w, h = nueva.shape
# Creación de una imagen nueva del mismo tamaño pero con puros 0
blur = np.zeros((w, h))
# Filtrado medio o suavizado de la imagen
for row in range(h-1):
    for col in range(w-1):
        blur[row+1][col+1] = (nueva[row+1][col+1] + nueva[row+1][col+1] + nueva[row+1][col+1]
                              + nueva[row+1][col+1] + nueva[row+1][col+1] + nueva[row+1][col+1]
                              + nueva[row+1][col+1] + nueva[row+1][col+1] + nueva[row+1][col+1]) / 9
        if blur[row+1][col+1] < 0:
            blur[row+1][col+1] = 0
# Conversión del resultado a 8 bits
blur = np.uint8(blur)
# Copia de la imagen suavizada
nueva2 = blur.copy()
# Se obtienen las dimensiones de la imagen suavizada
w2, h2 = nueva2.shape
# Creación de otra imagen con puros 0
thresh = np.zeros((w2, h2))
# Picos del histograma
P1 = 215
P2 = 255
# Umbralización binaria invertida
for row in range(h2-1):
    for col in range(w2-1):
        thresh[row][col] = nueva2[row][col]
        if nueva2[row][col] < P1 or nueva2[row][col] >= P2:
            thresh[row][col] = 0
        else:
            thresh[row][col] = 255
# Conversión del resultado a 8 bits
thresh = np.uint8(thresh)
# Copia de la imagen binarizada
contorno = thresh.copy()
# contornos y jerarquía -
# cv2.RETR_EXTERNAL - Regresa como salida los contornos externos extremos
# cv2.CHAIN_APPROX_SIMPLE - Considera solo segmentos horizontales, verticales y diagonales
cnts, hrchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Recorrido de cada índice dentro del vector de contornos
for cnt in cnts:
    # Determinar área de los contornos
    area = cv2.contourArea(cnt)
    # si el area es mayor a 0, obtener las coordenadas del contorno
    if area > 0:
        pass
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(contorno, (x, y), (x+w, y+h), (251, 255, 140), 2)

# Se determina la longitud del vector cnt y se igual con 6,
# ya que, son 6 pastillas dentro del blister
if len(cnt) == 6:
    print(f'Blister completo, contiene {len(cnt)} pastillas')
else:
    print("Blister incompleto")

cv2.imshow("Original", rees)
cv2.imshow("Grises", grises)
cv2.imshow("Ecualizacion de histograma", histo)
cv2.imshow("Umbralizacion", thresh)
cv2.imshow("Suavizado", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()