import cv2 as cv
import numpy as np
import os

def hsvColorSegmentation():
    # Get current directory and image path
    root = os.getcwd()
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")

    # Read and convert image
    img = cv.imread(imgPath)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Define HSV color range
    lowerbound = np.array([0, 0, 50])
    upperbound = np.array([10, 120, 100])

    # Create mask based on HSV range
    mask = cv.inRange(imgHSV, lowerbound, upperbound)

    # Resize the mask image for smaller display
    small_mask = cv.resize(mask, (1000, 1000))  # (width, height)

    # Display the resized mask
    cv.imshow('Resized Mask', small_mask)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Run the function
hsvColorSegmentation()
