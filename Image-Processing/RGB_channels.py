import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 

def PureColors():
    zeros = np.zeros((500, 500), dtype=np.uint8)
    ones = np.ones((500, 500), dtype=np.uint8)

    BlueImg = cv.merge((zeros, zeros, ones * 255))
    GreenImg = cv.merge((zeros, ones * 255, zeros))
    RedImg = cv.merge((ones * 255, zeros, zeros))
    WhiteImg = cv.merge((ones * 255, ones * 255, ones * 255))
    BlackImg = cv.merge((zeros, zeros, zeros))

    plt.figure(figsize=(15, 6))

    plt.subplot(2, 3, 1)
    plt.imshow(BlueImg)
    plt.title("Blue")
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(GreenImg)
    plt.title("Green")
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(RedImg)
    plt.title("Red")
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.imshow(WhiteImg)
    plt.title("White")
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(BlackImg)
    plt.title("Black")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

PureColors()
