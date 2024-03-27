import cv2
import numpy as np

# Define the frame width and height for the video capture
frameWidth = 640
frameHeight = 480

# Initialize the video capture object with camera index 0 (default camera)
cap = cv2.VideoCapture(0)

# Set the frame width, height, and brightness
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


# Function to be called by the trackbars (does nothing)
def empty(a):
    pass


# Create a window named "HSV" and resize it
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

# Create trackbars for setting HSV range thresholds
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

# Main loop for capturing frames and processing
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Convert the frame from BGR to HSV color space
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current trackbar positions for HSV range thresholds
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # Create arrays for lower and upper bounds of HSV range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask to filter pixels within the specified HSV range
    mask = cv2.inRange(imgHsv, lower, upper)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(img, img, mask=mask)

    # Convert the mask to BGR for visualization
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Stack the original frame, mask, and result horizontally
    hStack = np.hstack([img, mask, result])

    # Display the horizontally stacked images
    cv2.imshow("Horizontal Stacking", hStack)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()


