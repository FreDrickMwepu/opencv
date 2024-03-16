import cv2
import numpy as np

# Define frame width and height
frameWidth = 1280
frameHeight = 720

# Open the webcam (Change the parameter to 0 if using built-in webcam, 1 if using an external webcam)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

# Set frame width, height, and brightness (adjust this value according to your environment)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)  # Brightness adjustment

# Define colors to be detected in HSV format
myColors = [[5, 107, 0, 19, 255, 255],    # Orange
            [133, 56, 0, 159, 156, 255],  # Purple
            [57, 76, 0, 100, 255, 255],   # Green
            [0, 0, 200, 179, 40, 255]]    # White

# Function to find specified colors in an image
def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])  # Lower HSV values for the color
        upper = np.array(color[3:6])  # Upper HSV values for the color
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResults, (x, y), 10, (255, 0, 0), cv2.FILLED)
        # cv2.imshow(str(color[0]), mask)

# Get Contours Function
def getContours(img):
    imgContour = img.copy()  # Add this line to initialize imgContour
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResults, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y
# Main loop
while True:
    # Read frame from webcam
    success, img = cap.read()

    # Display
    imgResults = img.copy()

    # Find specified colors in the frame
    findColor(img, myColors)

    # Display the original frame
    cv2.imshow("Fredrick", imgResults)

    # Exit loop if 'q' is pressed (wait for 1 millisecond)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()