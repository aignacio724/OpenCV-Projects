#!/usr/bin/python

''' This is a simple program to display a color palette and
    track bar for RGB values. Which can be modified and corresponding
    values will display the correct color on screen.
    -----------------------------------------------------------------
    Goal: Learn to bind trackbar to OpenCV windows
          Learn about cv2.getTrackbarPos(), cv2.createTrackbar(), etc.'''

# cv2.getTrackbarPos()
# arg1 is trackbar name
# arg2 is window name
# arg3 is default value
# arg4 is max value
# arg5 is callback function which is executed everytime trackbar value changes

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, this will display the color 
# from the given RGB values
img = np.zeros((300,512,3), np.uint8)

# Label the new window
cv2.namedWindow('RGB Colors')

# create trackbars for color change
cv2.createTrackbar('R', 'RGB Colors',0,255,nothing)
cv2.createTrackbar('G', 'RGB Colors',0,255,nothing)
cv2.createTrackbar('B', 'RGB Colors',0,255,nothing)


while True:
    cv2.imshow('RGB Colors', img)
    
    # Poll for keyboard interrupt, if 'q' quit
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    # get current positions of  trackbars
    red = cv2.getTrackbarPos('R', 'RGB Colors')
    green = cv2.getTrackbarPos('G', 'RGB Colors')
    blue = cv2.getTrackbarPos('B', 'RGB Colors')
    
    # Display the color in the image with the new RGB values
    img[:] = [blue,green,red]
    
    # Create a numpy uint8 array, this will be used to convert 
    # the RGB values to HSV
    color = np.uint8([[[blue,green,red]]])
    
    # Convert the RGB values to HSV
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    # Print the HSV values to the command prompt
    print "-" * 10
    print hsv


cv2.destroyAllWindows()
