import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
import os

def WebCamToFile():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')


    root = os.getcwd()
    outPath = os.path.join(root,'Video-Processing\\Videos\\captured_video.avi')
    out = cv.VideoWriter(outPath,fourcc,20.0,(640,480))


    if not cap.isOpened():
        print("WebCam not opened ! ")
        exit()
    while cap.isOpened() :
        ret , frame = cap.read()
        if ret : 
            cv.imshow('webcam',frame)
            out.write(frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    WebCamToFile()
    