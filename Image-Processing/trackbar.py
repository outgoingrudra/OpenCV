import cv2 as cv
import numpy as np
import os

# Global variables
drawing = False
last_x, last_y = -1, -1
line_thickness = 5  

def nothing(x):
    pass  

def draw_line(event, x, y, flags, param):
    global drawing, last_x, last_y, line_thickness
    img = param

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.line(img, (last_x, last_y), (x, y), (255, 255, 255), thickness=line_thickness)
            last_x, last_y = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.line(img, (last_x, last_y), (x, y), (255, 255, 255), thickness=line_thickness)

def TrackbarDrawing():
    global line_thickness

    # Get image
    root = os.getcwd()
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)
    img = cv.resize(img, (800, 600))

    windowName = 'Trackbar Drawing App'
    cv.namedWindow(windowName)

    # Create trackbar (0-50 thickness)
    cv.createTrackbar('Thickness', windowName, line_thickness, 50, nothing)

    cv.setMouseCallback(windowName, draw_line, img)

    while True:
        # Update line thickness from trackbar
        line_thickness = cv.getTrackbarPos('Thickness', windowName)

        cv.imshow(windowName, img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

TrackbarDrawing()
