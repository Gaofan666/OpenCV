import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画一个等腰三角形
points = np.array([(300, 10), (150, 100), (450, 100)], np.int32)  # 存放点
cv2.polylines(img, [points], True, (0, 0, 255),3)

cv2.fillPoly(img,[points],(255,0,0))

cv2.imshow('img', img)
cv2.waitKey()
