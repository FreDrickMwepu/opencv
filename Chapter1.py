import cv2

frameWidth = 1280
frameHeight = 720

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()
    cv2.imshow("Fredrick", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break