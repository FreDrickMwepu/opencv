import cv2  # this import the OpenCV library

# Load the pre-trained face detection classifier from file
faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")

# Read the image file
img_lena1 = cv2.imread('Resources/lena.jpeg')
img_lena2 = cv2.imread('Resources/lady.jpg')

# Convert the image to grayscale, as face detection typically works better on grayscale images
imgGray1 = cv2.cvtColor(img_lena1, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(img_lena2, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image using the detectMultiScale function
# This function returns a list of rectangles where faces are detected
# The scaleFactor and minNeighbors parameters affect the quality and robustness of the detection
faces1 = faceCascade.detectMultiScale(imgGray1, 1.1, 4)
faces2 = faceCascade.detectMultiScale(imgGray2, 1.1, 4)

# Loop through each detected face
for (x, y, w, h) in faces1:
    # Draw a rectangle around each detected face
    # Parameters: image, top-left corner coordinates, bottom-right corner coordinates, color, thickness
    cv2.rectangle(img_lena1, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.rectangle(img_lena1, (x, y), (x + w, y + h), (255, 0, 0), 2)
for (x, y, w, h) in faces2:
    # This is going to draw a rectangle around each detected face on the second image which lad.jpeg
    # This also has the same parameters as the ones on top
    cv2.rectangle(img_lena2, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.rectangle(img_lena2, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the image with rectangles drawn around detected faces
cv2.imshow("Result1", img_lena1)
cv2.imshow("Result2", img_lena2)


# Wait for any key press to close the displayed image
cv2.waitKey(0)


