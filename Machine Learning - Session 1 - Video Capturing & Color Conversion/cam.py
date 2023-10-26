#Importing Libraries 

import cv2 
import numpy as np



cap = cv2.VideoCapture(1) #Assign the camera to open
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height


while (1) :#Program Main Loop
    
    ret, img = cap.read() #read the frame from camera
    
    cv2.imshow('img',img) #Open the output window for displaying image

   

    k=cv2.waitKey(30) #delay for 30 millseconds after reading the each frame
    if k == ord('q'):# break condition
        break 


cap.release()#releasing the opened camera
cv2.destroyAllWindows()#close the windows opened by cv
