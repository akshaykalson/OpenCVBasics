import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow('TrackBars')  #creates empty window
cv2.resizeWindow('TrackBars', 640,240 )
cv2.createTrackbar('Hue Min', 'TrackBars', 55, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)

while True:

    img = cv2.imread('resources/cutie.jpg')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    hue_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    sat_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    sat_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    val_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    val_max = cv2.getTrackbarPos('Val Max', 'TrackBars')

    lowerlimit = np.array([hue_min, sat_min, val_min])
    upperlimit = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV,lowerlimit, upperlimit)
    imgResult = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('new HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('with Mask', imgResult)

    cv2.waitKey(1)