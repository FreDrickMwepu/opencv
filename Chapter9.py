import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img_lena = cv2.imread('Resources/lena.jpeg')
imgGray = cv2.cvtColor(img_lena, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

// Hello world

for (x, y, w, h) in faces:
    cv2.rectangle(img_lena, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img_lena)
cv2.waitKey(0)