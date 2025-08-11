import cv2 as cv
import numpy as np
import os

def drawCircle(event, x, y, flags, param):
    img = param
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 10, (0, 0, 225), -1)

def DoubleClickDrawing():
    # Get current directory and image path
    root = os.getcwd()
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)

    # Resize image (width=800, height=600)
    img = cv.resize(img, (800, 600))

    windowName = 'Drawing App'
    cv.namedWindow(windowName)
    cv.setMouseCallback(windowName, drawCircle, img)

    while True:
        cv.imshow(windowName, img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

DoubleClickDrawing()
