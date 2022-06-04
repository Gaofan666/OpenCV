import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# # 绘制一个矩形，线宽5
# cv2.rectangle(img,(0,0),(200,200),(0,0,255),5)
# # 如果改成 -1 这个矩形就是填充矩形
# cv2.rectangle(img,(500,10),(620,300),(0,0,255),-1)

# 绘制一个圆
# cv2.circle(img,(320,240),150,(255,255,0),-1)

# 绘制一个椭圆
cv2.ellipse(img, (320, 240), (200, 100), 0, 0, 360, (0, 0, 255), 2)

cv2.imshow('ellipse', img)
cv2.waitKey()
