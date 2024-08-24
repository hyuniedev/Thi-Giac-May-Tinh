import cv2

cap = cv2.VideoCapture(0)  # Mở camera mặc định

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()  # Đọc một khung hình

    if not ret:
        break  # Thoát nếu không đọc được khung hình
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # Chuyển lại về BGR
    
    gray = cv2.flip(gray, 1)  # Lật hình
    
    out.write(gray)
    
    cv2.imshow('Video', gray)  # Hiển thị khung hình

    if cv2.waitKey(1) == ord('q'):  # Thoát khi nhấn phím 'q'
        break

cap.release()  # Giải phóng tài nguyên camera
out.release()
cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ
