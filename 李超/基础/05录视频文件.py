import cv2

# 创建VideoWriter为多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('img/out.mp4', fourcc, 25, (1920, 1080))

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 1920, 1080)

cap = cv2.VideoCapture(0)

while cap.isOpened():  # 判断摄像头是否打开
    ret, frame = cap.read()
    if ret:  # 判断是否为True，读到一帧显示一帧，如果为False，则不显示
        cv2.imshow('video', frame)
        vw.write(frame)  # 写数据到多媒体文件

        key = cv2.waitKey(1)
        if key == 113:
            break
    else:
        break

cap.release()
vw.release()
cv2.destroyAllWindows()
