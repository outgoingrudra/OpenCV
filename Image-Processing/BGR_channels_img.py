import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os

def All_BGRChannel():
    # Get current directory and image path
    root = os.getcwd()
    print("Current directory:", root)
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")

    # Read image
    img = cv.imread(imgPath)
    
    if img is None:
        print("Image not found at:", imgPath)
        return

    # Resize image to smaller size
    img = cv.resize(img, (400, 400))

    # Split BGR channels
    b, g, r = cv.split(img)
    zeros = np.zeros_like(b)

    # Isolate each channel
    bChannel = cv.merge((b, zeros, zeros))
    gChannel = cv.merge((zeros, g, zeros))
    rChannel = cv.merge((zeros, zeros, r))

    # Convert to RGB for matplotlib display
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    bChannelRGB = cv.cvtColor(bChannel, cv.COLOR_BGR2RGB)
    gChannelRGB = cv.cvtColor(gChannel, cv.COLOR_BGR2RGB)
    rChannelRGB = cv.cvtColor(rChannel, cv.COLOR_BGR2RGB)

    # Display original and channel images
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(imgRGB)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(bChannelRGB)
    plt.title("Blue Channel")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(gChannelRGB)
    plt.title("Green Channel")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(rChannelRGB)
    plt.title("Red Channel")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

All_BGRChannel()
