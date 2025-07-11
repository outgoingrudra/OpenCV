import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os


def readImage():
    root = os.getcwd()
    print(root)
    imgPath = os.path.join(root,'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)

    cv.imshow('img',img)
    cv.waitKey(0)

def writeImage():
    root = os.getcwd()
    print(root)
    imgPath = os.path.join(root,'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)

    outPath=os.path.join(root,'Image-Processing', "copied_Image.jpg")
    cv.imwrite(outPath,img)

    

if __name__ == '__main__' :
    #readImage()
    writeImage()