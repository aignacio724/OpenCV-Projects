#!/usr/bin/python

# OpenCV Python tutorial on Writing an Image

import numpy as np
import cv2

# Load a color image
img = cv2.imread('godzilla.jpg', -1)

# Display the image
# cv2.imshow() : first argument is the window name, second argument is the image 
cv2.imshow('Godzilla', img)

# convert the colored image to grayscale
# cv2.cvtColor(src, code) : Convert input image from one color space to another
# src  : input image
# code : color space convertion

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray Godzilla', grayImg)

# save a grayscale version of the image
# cv2.imwrite() : first argument is the file name, second argument is the image we want to save
#cv2.imwrite('godzillagray.png', grayImg)

# cv2.waitKey is a keyboard binding function. Its argument is the time in milliseconds.
key = cv2.waitKey(0) & 0xFF

# Save the image if the 's' key is pressed
if key == ord('s'):
    cv2.imwrite('godzillagray.png', grayImg)
    
# This function simply destroys all the windows we created.
cv2.destroyAllWindows()
