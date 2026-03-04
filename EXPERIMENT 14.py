import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\Downloads\DHONI 2.jpg")

# Define 4 source points (change if needed)
pts1 = np.float32([[50,50], [300,50], [50,300], [300,300]])

# Define destination points
pts2 = np.float32([[0,0], [250,0], [0,250], [250,250]])

# Get transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transform
result = cv2.warpPerspective(img, matrix, (250,250))

# Show output
cv2.imshow("Output", result)
cv2.waitKey(0)
cv2.destroyAllWindows()