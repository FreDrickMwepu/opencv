import cv2
import numpy as np

# This initializes frame width and height
frameWidth = 640
frameHeight = 480

# The next Line will open webcam (Change the parameter to 0 if using built-in webcam, 1 if using an external webcam)
cap = cv2.VideoCapture(1)

# Set frame width and height
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Function to handle trackbar adjustments
def empty(a):
    pass

# Create window for HSV trackbars
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

# Create trackbars for HSV values
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

# Main loop for adjusting HSV values
while True:
    # Read frame from webcam
    success, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # Create lower and upper bounds for HSV range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create mask to filter colors within specified HSV range
    mask = cv2.inRange(imgHsv, lower, upper)

    # Apply mask to original image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Convert mask to BGR for displaying purposes
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Horizontally stack original image, mask, and result
    hStack = np.hstack([img, mask, result])

    # Display horizontally stacked images
    cv2.imshow('Horizontal Stacking', hStack)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()