import cv2 as cv
import numpy as np
import math

drawable = False
mode = True
ix, iy = -1, -1

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def draw_callback(event,x,y,flags,params):
    global ix, iy, drawable, mode
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawable = True
        ix, iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawable:
            if mode:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(ix,iy),int(distance(ix,iy,x,y)),(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawable = False
        if mode:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(ix,iy),int(distance(ix,iy,x,y)),(0,0,255),-1)
                
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_callback)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord("m"):
        mode = not mode
    elif k == ord("q"):
        break
    
cv.destroyAllWindows()