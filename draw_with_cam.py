import cv2
import numpy as np

vdo = cv2.VideoCapture(0)

height = int(vdo.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vdo.get(cv2.CAP_PROP_FRAME_WIDTH))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('draw.avi',fourcc,20.0,(width,height))

r = 30
tam = [width-60,60]
lineHorizontalStart = (tam[0]-30,tam[1])
lineHorizontalEnd = (tam[0]+30,tam[1])
lineVerticalStart = (tam[0],tam[1]-30)
lineVerticalEnd = (tam[0],tam[1]+30)
red = (0,0,255)

board = np.zeros((height,width,4),np.uint8)

while 1:
    ret , frame = vdo.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    
    brg_colorGetted = frame[tam[1],tam[0]]
    hsv_colorGetted = cv2.cvtColor(np.uint8([[brg_colorGetted]]),cv2.COLOR_BGR2HSV)
    hsvColor = hsv_colorGetted[0][0]
    
    lowerColor = np.array([hsvColor[0]-10,hsvColor[1]-40,hsvColor[2]-40])
    upperColor = np.array([hsvColor[0]+10,hsvColor[1]+40,hsvColor[2]+40])
    
    mask = cv2.inRange(cv2.cvtColor(frame,cv2.COLOR_BGR2HSV),lowerColor,upperColor)
    # --------------------------------------------
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Chọn contour lớn nhất (có thể là tay của bạn)
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Tính toán moments để tìm tọa độ trung tâm của contour
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            
            # Vẽ lên bảng trắng theo vị trí của tay
            cv2.circle(board, (cx, cy), 10, (0, 0, 255), -1)  # Đổi (0, 0, 255) thành màu bạn muốn
            
            # Hiển thị vòng tròn vị trí trên hình ảnh đầu vào
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), 2)
    # --------------------------------------------
    

    
    
    frame[height-60 : height-10, 50 : 100] = hsvColor
    
    frame = cv2.circle(frame,tam,r,red,2)
    frame = cv2.line(frame,lineHorizontalStart,lineHorizontalEnd,color = red, thickness=1)
    frame = cv2.line(frame,lineVerticalStart,lineVerticalEnd,color = red, thickness = 1)
    
    cv2.imshow('Draw with cam',frame)
    out.write(frame)
    
    if cv2.waitKey(2) == ord("q"):
        break
    
vdo.release()
out.release()
cv2.destroyAllWindows()
    
    
