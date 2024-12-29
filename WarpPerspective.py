import cv2
import numpy as np

img = cv2.imread('resources/cards.jpg')
width, height = 250, 650
pts1= np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])

matrix =cv2.getPerspectiveTransform(pts1, pts2)
imgWarped = cv2.warpPerspective(img, matrix, (width, height))

print(matrix)
# cv2.imshow('Card Image', img)
# cv2.imshow('Warped Image', imgWarped)
# cv2.waitKey(0)