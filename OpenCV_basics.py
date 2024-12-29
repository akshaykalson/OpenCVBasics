import cv2
import numpy as np

#now we will learn how to capture videos
# if we want to take video from a stored one
# cap = cv2.VideoCapture('Resources/test_video.mp4')
# but if we want to use webcam
# cap = cv2.VideoCapture(0)
# while True:
#     success, vid = cap.read()
#     cv2.imshow('Video', vid)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     #this above statement to break the loop is crucial while playing a video


#now we will take a look at some basic functions regarding images
img= cv2.imread('Resources/cutie.jpg') #to import an image
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #to convert that image to grascale
imgBlur = cv2.GaussianBlur(img, (9,9), 0) # kernel size tells the size of blur , must be odd number
imgCanny = cv2.Canny(img, 100,100) #function used for edge detection , larger the threshold number, more grained edge detection

#defining kernel for imgDilation
kern = np.ones((5,5), np.uint8)
imgDilation= cv2.dilate(imgCanny,kern, iterations=1) #this function will make the edges quite thick
imgErode= cv2.erode(imgDilation, kern, iterations=1)
cv2.imshow('Erode', imgErode)
cv2.waitKey(0)
cv2.imshow('Dilation', imgDilation)
cv2.waitKey(0)







