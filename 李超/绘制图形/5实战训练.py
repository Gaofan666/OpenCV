import cv2
import numpy as np

curshape = 0
startpoint = (0, 0)
img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow('draw', cv2.WINDOW_NORMAL)


# 定义鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    global curshape, startpoint, img  # 声明全局变量
    # 在起始点和终止点之间，鼠标按下点--鼠标抬起点
    if event == cv2.EVENT_LBUTTONDOWN:
        startpoint = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        # 左键抬起，开始画图型，先判断是什么图形
        if curshape == 0:
            cv2.line(img, startpoint, (x, y), (0, 0, 255))
        elif curshape == 1:
            cv2.rectangle(img, startpoint, (x, y), (0, 255, 255))
        elif curshape == 2:
            a = x - startpoint[0]
            b = y - startpoint[1]
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv2.circle(img, startpoint, r, (255, 0, 0))
        else:
            print('没有这个图形')
    elif event == cv2.EVENT_MBUTTONDOWN:  # 中键清空屏幕
        img = np.zeros((480, 640, 3), np.uint8)


cv2.setMouseCallback('draw', mouse_callback, "a")

while True:
    cv2.imshow('draw', img)
    key = cv2.waitKey(1)
    # if key>0:
    #     print('key=', key)  # q 113   l 108   c 99    r 114
    if key == 113:
        break
    elif key == 108:
        curshape = 0  # 线
    elif key == 114:
        curshape = 1  # 矩形
    elif key == 99:
        curshape = 2  # 圆

cv2.destroyAllWindows()
