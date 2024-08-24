import cv2 as cv
import numpy as np

imgDog = cv.imread('dog.png',cv.IMREAD_COLOR)

imgDog_HSV = cv.cvtColor(imgDog,cv.COLOR_BGR2HSV)

while 1:

    mark = cv.inRange(imgDog_HSV,np.array([20,100,100]),np.array([30,255,255]))
    
    mark_img = cv.bitwise_and(imgDog,imgDog,mask = mark)

    cv.imshow('orinal image',imgDog)
    cv.imshow('img Dog hsv', imgDog_HSV)
    cv.imshow('mark yellow', mark)
    cv.imshow('img add mark', mark_img)
    
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv.destroyAllWindows()