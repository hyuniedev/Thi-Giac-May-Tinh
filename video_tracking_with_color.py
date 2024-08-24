import cv2
import numpy as np

vdo = cv2.VideoCapture(0)

height = int(vdo.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vdo.get(cv2.CAP_PROP_FRAME_WIDTH))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('vd_getColor.avi',fourcc,20.0,(width,height))

while 1:
    ret , frame = vdo.read()
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    
    frame2HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mark_blue = cv2.inRange(frame2HSV,lower_blue,upper_blue)
    
    frame_fild = cv2.bitwise_and(frame,frame,mask=mark_blue)
    
    cv2.imshow('Video check', frame_fild)
    out.write(frame_fild)
    
    if cv2.waitKey(2) == ord("q"):
        break
    
vdo.release()
out.release()
cv2.destroyAllWindows()
    
    
