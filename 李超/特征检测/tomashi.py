import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')

maxCorners = 1000
ql = 0.01
minDistance = 10

# 灰度化才能进行角点检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Harris角点检测
corners = cv2.goodFeaturesToTrack(gray, maxCorners, ql, minDistance)
corners = np.int0(corners)

# 绘制角点
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('tomas', img)

cv2.waitKey(0)
