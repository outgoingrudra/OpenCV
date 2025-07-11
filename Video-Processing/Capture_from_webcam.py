import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os

def captureWebCam():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("WebCam not opened ! ")
        exit()
    while True :
        ret , frame = cap.read()
        if ret : 
            cv.imshow('webcam',frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    captureWebCam()
    