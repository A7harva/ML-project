import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(1)
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height
while (1) :
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow('img',img)
    k=cv2.waitKey(30) 
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
