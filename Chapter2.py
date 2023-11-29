import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpeg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations= 1)
imgEroded = cv2.erode(imgDilation, kernel, iterations= 1)

cv2.imshow(" A Gray Image of Lena", imgGray)
cv2.imshow("A Blur image of Lena", imgBlur)
cv2.imshow("An edge detected Image of Lena", imgCanny)
cv2.imshow("A dilated Image of lena", imgDilation)
cv2.imshow("An Eroded Image of lena", imgEroded)
cv2.waitKey(0)