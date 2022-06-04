import cv2
import numpy as np


# 定义鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


# 创建窗口
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 480)

# 设置回调
cv2.setMouseCallback('mouse', mouse_callback, '调用回调函数')

# 利用numpy设置一个黑色的背景
img = np.zeros((480, 640, 3))
while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)
    if key == 113:
        break

cv2.destroyAllWindows()
