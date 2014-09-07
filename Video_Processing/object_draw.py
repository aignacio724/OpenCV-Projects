#!/usr/bin/python

''' This is a simple object tracking program using
    OpenCV-Python. Use color thresholding to adjust color tracking'''

# Color conversion flags 
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2HSV

import cv2
import numpy as np

# Initialize the Camera
capture = cv2.VideoCapture(-1)
cv2.namedWindow('Video Feed')

# Globals used for drawing function
drawing = False
ix,iy = -1,-1

def draw_rect(event,x,y,flags,param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        print "pressed"
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        print "move"
        if drawing == True:
            cv2.rectangle(overlay,(ix,iy),(x,y),(0,255,0),1)
    elif event == cv2.EVENT_LBUTTONUP:
        print "depressed"
        drawing = False
        cv2.rectangle(overlay,(ix,iy),(x,y),(0,255,0),1)


cv2.setMouseCallback('Video Feed', draw_rect)

while True:

    # Take each frame of the video feed
    returnVal , frame = capture.read()
    overlay = frame.copy()

    if returnVal != True:
        print "!!!!! Error getting frame\n"
    
    # Convert BGR to HSV
    cv2.addWeighted(overlay, 0.4, frame, 1 - 0.4, 0, frame)
    cv2.imshow('Video Feed',frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()

