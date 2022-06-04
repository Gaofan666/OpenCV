import cv2
import numpy as np

# 这里虽然写的是480*640  但是numpy是反着来的，img真实大小是640*480
img = np.zeros((480, 640, 3), np.uint8)

# 画线  红色的线  这里的坐标就是真实坐标
cv2.line(img, (0, 240), (640, 240), (0, 0, 255))
# 画一条蓝色的线  线宽 5
cv2.line(img, (320, 0), (320, 480), (255, 0, 0),5)

cv2.imshow('line', img)
cv2.waitKey()



