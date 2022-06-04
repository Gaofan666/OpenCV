import cv2
import numpy as np


# 定义一个函数，连接appros里面的点
def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 255, 0), 2)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 255, 0), 2)
        i = i + 1


img = cv2.imread('../img/hand.png')
# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('img', img)
# 轮廓查找
contours, hierarchy = cv2.findContours(bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)  # 打印出找到的角点

# 绘制轮廓,可以在bin上绘制，也可以在img绘制,需要注意的是img是三通道。bin是单通道
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# 多边形逼近
e = 20  # 精度
appros = cv2.approxPolyDP(contours[0], e, True)
drawShape(img, appros)
print('appros=',appros)

# 凸包
hull = cv2.convexHull(contours[0])
drawShape(img,hull)

cv2.imshow('result', img)

cv2.waitKey(0)
