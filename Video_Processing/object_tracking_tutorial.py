#!/usr/bin/python

''' This is a simple object tracking program using
    OpenCV-Python.'''

# Color conversion flags 
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2HSV

import cv2
import numpy as np

capture = cv2.VideoCapture(-1)

while True:

    # Take each frame of the video feed
    returnVal , frame = capture.read()
    
    if returnVal != True:
        print "!!!!! Error getting frame\n"
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define ranges for color detection in HSV
    # For this program blue
    lower_color = np.array([110,50,50])
    upper_color = np.array([130,255,255])
    
    # Threshold the HSV image to get only defined color, blue in this case
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

