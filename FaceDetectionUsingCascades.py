import cv2

faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

# img = cv2.imread('resources/Elon Test.jpg')

cap = cv2.VideoCapture(0)
while True:
    success, img= cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('Webcam  ', img)
    cv2.waitKey(1)
