import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os


def readWriteSinglePixel() :
    root = os.getcwd()
    print(root)
    imgPath = os.path.join(root,'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    print(imgRGB[312,350])
  
if __name__ == '__main__' :
    readWriteSinglePixel()