import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os

def ConvertToGray():
    root = os.getcwd()
    print("Current directory:", root)
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")

    img = cv.imread(imgPath)
    
    if img is None:
        print("Image not found at:", imgPath)
        return

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    plt.figure()
    plt.imshow(imgGray, cmap='gray')  # ✅ Fix here
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

ConvertToGray()
