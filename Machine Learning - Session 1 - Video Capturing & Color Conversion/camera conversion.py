#Importing Libraries 

import cv2 
import numpy as np



cap = cv2.VideoCapture(1) #Assign the camera to open
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height


while (1) :#Program Main Loop
    
    ret, img = cap.read() #read the frame from camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converting imge to grayscale
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#converting imge to hsv

   #Open the output window for each conversion and display the output
    cv2.imshow('img',img)
    cv2.imshow('gray',gray)
    #cv2.imshow('hsv',hsv)

   

    k=cv2.waitKey(30) #delay for 30 millseconds after reading the each frame
    if k == ord('q'):# break condition
        break 


cap.release()#releasing the opened camera
cv2.destroyAllWindows()#close the windows opened by cv
