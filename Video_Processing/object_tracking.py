#!/usr/bin/python

''' This is a simple object tracking program using
    OpenCV-Python. Use color thresholding to adjust color tracking'''

# Color conversion flags 
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2HSV

import cv2
import numpy as np

def nothing(x):
    pass

# Initialize the Camera
capture = cv2.VideoCapture(-1)

# Create the two threshold boxes
# Used for adjusting color for object tracking
cv2.namedWindow('Color Adjust')


# Create trackbars for color change
window1 = np.zeros((128,512,3), np.uint8)
cv2.createTrackbar('R','Color Adjust',255,255,nothing)
cv2.createTrackbar('G','Color Adjust',0,255,nothing)
cv2.createTrackbar('B','Color Adjust',0,255,nothing)

thresh_ammount = 10

# Set and create the hsv thresholds (lower and upper)  
# the desired color in my case lower end [low_hue, 50 ,50] and [high_hue, 255,255]
low_sat,low_val = (50,50)
high_sat,high_val = (255,255)


while True:

    cv2.imshow('Color Adjust', window1)

    # Take each frame of the video feed
    returnVal , frame = capture.read()
    
    if returnVal != True:
        print "!!!!! Error getting frame\n"
    
    # Get the RGB values from the trackbar window 
    red   = cv2.getTrackbarPos('R', 'Color Adjust')
    green = cv2.getTrackbarPos('G', 'Color Adjust')
    blue  = cv2.getTrackbarPos('B', 'Color Adjust')
    window1[:] = [blue,green,red]
    
    # Convert BGR to HSV
    color_img = np.uint8([[[blue,green,red]]])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_thresh = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
    
    # Retrive the Hue value of the RGB -> HSV image conversion
    hue = hsv_thresh[0][0][0]

    # Add or subtract from the hue value for thresholding
    # Depending on Hue value, subtrac or add threshold value
    if hue < 10: 
        low_hue = hue
        high_hue = hue + thresh_ammount 
    elif hue > 245:
        low_hue = hue - thresh_ammount
        high_hue = hue
    else: 
        low_hue = hue - thresh_ammount 
        high_hue = hue + thresh_ammount 

    # Set and create the hsv thresholds (lower and upper)  
    low_hsv = np.array([low_hue,low_sat,low_val])
    high_hsv = np.array([high_hue,high_sat,high_val])
    
    # Threshold the HSV image to get only defined color, blue in this case
    mask = cv2.inRange(hsv, low_hsv, high_hsv)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('Video Feed',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

