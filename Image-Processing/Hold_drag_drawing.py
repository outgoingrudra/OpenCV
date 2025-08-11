import cv2 as cv
import numpy as np
import os

# Global variables
drawing = False  
last_x, last_y = -1, -1

def draw_line(event, x, y, flags, param):
    global drawing, last_x, last_y
    img = param

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.line(img, (last_x, last_y), (x, y), (255, 255, 255), thickness=8)
            last_x, last_y = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.line(img, (last_x, last_y), (x, y), (255, 255, 255), thickness=8)

def DragDrawing():
    # Get image
    root = os.getcwd()
    imgPath = os.path.join(root, 'Image-Processing', "cat.jpg")
    img = cv.imread(imgPath)

    # Resize image
    img = cv.resize(img, (800, 600))

    windowName = 'Drag Drawing App'
    cv.namedWindow(windowName)
    cv.setMouseCallback(windowName, draw_line, img)

    while True:
        cv.imshow(windowName, img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

DragDrawing()
