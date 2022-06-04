import cv2

# 创建窗口
cv2.namedWindow('new', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',640,480)
cv2.resizeWindow('new2',480,640)
cv2.imshow('new', 0)  # 显示框口
cv2.imshow('new2', 0)  # 显示框口

while True:
    # 不断接收键盘按键
    key = cv2.waitKey(0)  # 接收键盘事件，如果输入q，则退出
    if key == 113:  # 按键q
        print("退出")
        break
cv2.destroyAllWindows()