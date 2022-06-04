import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

# 获取视频设备
cap = cv2.VideoCapture('img/ex02.mp4')

while True:
    # 获取视频
    ret,frame = cap.read()
    cv2.imshow('video',frame)

    # 这里如果填0,则一直等待键盘事件，只能获取到一帧视频帧然后就停住了
    key = cv2.waitKey(66)
    if key == 113:
        break
# 释放资源
cap.release()
cv2.destroyAllWindows()