import cv2

path1 = 'chicles/Pepto1-1.jpeg'
path2 = 'chicles/Pepto1-2.jpeg'

img = cv2.imread(path2)
rees = cv2.resize(img, (720, 640))
grises = cv2.cvtColor(rees, cv2.COLOR_BGR2GRAY)
histo = cv2.equalizeHist(grises, cv2.CV_64F)
blur = cv2.medianBlur(histo, 3)
ret, thresh = cv2.threshold(blur, 215, 255, cv2.THRESH_BINARY)
contorno = thresh.copy()
cnts, hrchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area > 900:
        pass
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(contorno, (x, y), (x+w, y+h), (251, 255, 140), 2)


if len(cnt) == 6:
    print(f'Blister completo, contiene {len(cnt)} pastillas')
else:
    print("Blister incompleto")


cv2.imshow("Original", rees)
cv2.imshow("Umbralizacion", thresh)
cv2.imshow("Grises", grises)
cv2.imshow("Ecualizacipon de histograma", histo)
cv2.imshow("Suavizado", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()