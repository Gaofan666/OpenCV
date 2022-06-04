import cv2
import numpy as np


def callback(a):
    pass


cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

img = np.zeros((480, 640, 3),np.uint8)
while True:
    # 读取trackbar的值
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    # 读取到r,g,b的值后对img进行操作
    img[:] = [b, g, r]  # 对img的所有像素赋值为刚才读取到的r,g,b值
    cv2.imshow('trackbar', img)
    key = cv2.waitKey(10)
    if key == 113:
        break

cv2.destroyAllWindows()
