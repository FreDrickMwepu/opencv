<<<<<<< HEAD
import cv2  # Import the OpenCV library

# Load the pre-trained face detection classifier from file
faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")

# Read the image file
img_lena = cv2.imread('Resources/lena.jpeg')

# Convert the image to grayscale, as face detection typically works better on grayscale images
imgGray = cv2.cvtColor(img_lena, cv2.COLOR_BGR2GRAY)
git
# Detect faces in the grayscale image using the detectMultiScale function
# This function returns a list of rectangles where faces are detected
# The scaleFactor and minNeighbors parameters affect the quality and robustness of the detection
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Loop through each detected face
for (x, y, w, h) in faces:
    # Draw a rectangle around each detected face
    # Parameters: image, top-left corner coordinates, bottom-right corner coordinates, color, thickness
    cv2.rectangle(img_lena, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with rectangles drawn around detected faces
cv2.imshow("Result", img_lena)

# Wait for any key press to close the displayed image
cv2.waitKey(0)

>>>>>>> origin/main
