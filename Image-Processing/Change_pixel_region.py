import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os


def ChangePixelRegion() :
    root = os.getcwd()
    print(root)
    imgPath = os.path.join(root,'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    
    plt.figure()
    plt.imshow(imgRGB)
    plt.title("Previously Image")
    plt.show()
    

    region = imgRGB[1000:1500,1000:1500]
    dx = 500
    dy = 500
    startX = 2600
    startY= 1700
    imgRGB[startX:startX+dx , startY:startY+dy] = region

    plt.figure()
    plt.imshow(imgRGB)
    plt.title("After Update , Image")
    plt.show()

ChangePixelRegion()