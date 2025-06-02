import cv2
import numpy as np
import time 

video = cv2.VideoCapture(0)
time.sleep(1)
count = 0 
background = 0 

for i in range(60) : 
    return_val, background = video.read()
    if return_val == False:
        continue

background = np.flip(background, axis = 1)
while True :
    status,frame = video.read()
    if not status:
        print("Cannot access camera")
        break
    count+=1
    img = np.flip(frame,axis = 1)
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([100,40,40])
    upper_red = np.array([100,255,255])
    
