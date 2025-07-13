import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os

def ReadAsGray():
    root = os.getcwd()
    print("Current directory:", root)
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")

    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Image not found at:", imgPath)
        return

   
    plt.figure()
    plt.imshow(img, cmap='gray')  # ✅ Fix here
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

ReadAsGray()
