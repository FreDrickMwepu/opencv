import cv2

import numpy as np

img = cv2.imread("Resources/car.jpeg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# The line below is a matrix that points out specific points that you would like to crop out
imgCropped = img[0:200, 200:500]

cv2.imshow("Car", img)
cv2.imshow("Image of the car Resized", imgResize)
cv2.imshow("Image of the car Cropped", imgCropped)
cv2.waitKey(0)