import cv2
import numpy as np

imgWhite= np.ones((512,512))
imgBlack = np.zeros((512,512))
imgColor= np.zeros((512,512,3), np.uint8)

imgColor[:]= (200,50,0) #in BGR format to create a color image

print(imgColor)
# cv2.line(imgColor, (0,0), (240,320), (0,0,255), 3)  #will draw a line for points 0,0 to 240,320
# cv2.line(imgColor, (0,0), (imgColor.shape[1], imgColor.shape[0]), (0,0,255), 3)  #will draw a line diagonal

cv2.rectangle(imgColor, (0,0), (350,250), (0,0,255), cv2.FILLED)
cv2.circle(imgColor,(450,250), 30, (0,255,0), 5)
cv2.putText(imgColor, "Open CV Practice", (50,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
# cv2.imshow('Zeros', imgBlack)
# cv2.imshow('Ones', imgWhite)
cv2.imshow('Color', imgColor)

 
cv2.waitKey(0)

