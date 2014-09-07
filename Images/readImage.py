#!/usr/bin/python

# OpenCV Python tutorial on reading in Images

import numpy as np
import cv2

''' Load an Image
    To read an Image, use the cv2.imread() function
    cv2.imread(filename[, flags])
    1 cv2.IMREAD_COLOR     : Loads a color image
    0 cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
   -1 cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel '''

# Load a color image in grayscale
img = cv2.imread('godzilla.jpg', 0)

# Display the image
# cv2.imshow() : first argument is the window name, second argument is the image
cv2.imshow('Grayscale', img)

# Display the color img in a resizable window. By default, the flag is cv2.WINDOW_AUTOSIZE
cv2.namedWindow('Resizable Color', cv2.WINDOW_NORMAL)
img2 = cv2.imread('godzilla.jpg', -1)
cv2.imshow('Resizable Color', img2)

# cv2.waitKey is a keyboard binding function. Its argument is the time in milliseconds.
cv2.waitKey(0)

# This function simply destroys all the windows we created.
cv2.destroyAllWindows()
