#!/usr/bin/python

''' This is a simple object tracking program using
    OpenCV-Python. Use color thresholding to adjust color tracking
    Try to draw a box around object of interest and get color range
    from object in region of interest'''

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
#global x1,y1,x2,y2
x1,y1 = -1,-1
x2,y2 = -1,-1

def draw_rect(event,x,y,flags,param):
    global x1,y1,x2,y2

    if event == cv2.EVENT_LBUTTONDOWN:
        print "pressed"
        x1,y1 = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        print "depressed"
        x2,y2 = x,y

cv2.setMouseCallback('Video Feed', draw_rect)

while True:

    # Take each frame of the video feed
    returnVal , frame = capture.read()

    if returnVal != True:
        print "!!!!! Error getting frame\n"
        break

##########
# TODO: Need to add a second window for drawing
#       Cannot draw directly onto video frame, each frame is over writting
#       mouse event
# DoNotNeed
##########

    #print "x1: %r y1: %r x2: %r y2: %r" % (x1,y1,x2,y2)
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    cv2.imshow('Video Feed',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()

