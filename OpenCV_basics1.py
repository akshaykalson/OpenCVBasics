import cv2
import numpy as np

#importing image
img= cv2.imread('Resources/cutie.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgResize = cv2.resize(img,(600,400)) #width comes first in the function, and then the height
imgCrop = img[400:900, 200:800]  #in this function, height is input first, and then the width

cv2.imshow("Cow", imgCrop)
cv2.waitKey(0)

#size of image
print(img.shape)

