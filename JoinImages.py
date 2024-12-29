import cv2
import numpy as np
img = cv2.imread('resources/cutie.jpg')
imgSmall = cv2.resize(img, (200,200))
horStack = np.hstack((imgSmall, imgSmall, imgSmall)) # this will put 3 of these images in one window
verStack = np.vstack((imgSmall, imgSmall))
cv2.imshow('Stack', horStack)
cv2.imshow('StackVer', verStack)
cv2.waitKey(0)





