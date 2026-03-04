import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\reddy\Downloads\dhoni-wallpaper-hd.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32 (required for Harris)
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate corner points (to make them visible)
corners = cv2.dilate(corners, None)

# Mark corners in red color
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Show the output image
cv2.imshow("Harris Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()