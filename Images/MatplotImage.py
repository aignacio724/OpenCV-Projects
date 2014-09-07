#!/usr/bin/python

# OpenCV Python tutorial on Writing an Image

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load a grayscale image
img = cv2.imread('godzilla.jpg',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
