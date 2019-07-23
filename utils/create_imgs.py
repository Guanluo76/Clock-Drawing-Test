import numpy as np
import cv2 as cv


def create_square():
    """
    Create a square shape image for tests.

    @return ndarray: img that contains a square
    """
    # create panel of size 100 x 100
    img = np.zeros((100, 100), dtype='uint8')

    # draw square of side 50 on the center, thickness 1
    cv.rectangle(img, (25, 25), (75, 75), (255, 0, 0), 1)

    return img

def create_circle():
    """
    Create a circle shape image for tests.

    @return ndarray: img that contains a circle
    """
    # create panel of size 100 x 100
    img = np.zeros((100, 100), dtype='uint8')

    # draw circle of radius 25 on the center, thickness 1
    cv.circle(img, (50, 50), 25, (255, 0, 0), 1)

    return img

