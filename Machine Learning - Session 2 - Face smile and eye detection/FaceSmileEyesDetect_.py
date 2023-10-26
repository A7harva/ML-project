import cv2
import numpy as np



face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')

cap=cv2.VideoCapture(1)
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        smiles=smile_cascade.detectMultiScale(roi_gray,1.5,15)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color,(sx,sy),((sx+sw),(sy+sh)),(0,0,255),2)
    for (p,q,w,h) in faces:
        cv2.rectangle(frame,(p,q),((p+w),(q+h)),(255,0,0),2)
        reg_gray=gray[q:q+h , p:p+w]
        reg_color = frame[q:q+h,p:p+w]
        eyes = eye_cascade.detectMultiScale(reg_gray,1.5,5)
        for (sp,sq,sw,sh) in eyes:
            cv2.rectangle(reg_color,(sp,sq),((sp+sw),(sq+sh)),(0,255,0),2)
   
    cv2.imshow('Video',frame)
   
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
