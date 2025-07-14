import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
time.sleep(1)
count = 0
background = 0

for i in range(60) :
    return_val, background = video.read()
    if return_val == False:
        continue

background = np.flip(background,axis=1)
while True:
    status,frame = video.read()
    if not status:
        print("Cant access camera")
        break
    count+=1
    img = np.flip(frame,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_green = np.array([99,50,10])
    upper_green = np.array([99,250,255])

    mask1 = cv2.inRange(hsv,lower_green,upper_green)

    lower_green = np.array([30,240,210])
    upper_green = np.array([255,250,255])

    mask2 = cv2.inRange(hsv,lower_green,upper_green)

    mask1 = mask1+mask2

    #refining the images

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.unit8),iterations = 2)
    mask1 = cv2.dilate(np.ones((3,3),np.unit8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)

    
