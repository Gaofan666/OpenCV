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


img = cv2.imread('../img/hello.jpeg')
# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('img', img)
# 轮廓查找
contours, hierarchy = cv2.findContours(bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('contours = ', contours)

# 绘制最小外接矩阵
r = cv2.minAreaRect(contours[1])
# 取出r中不包含角度的部分并且转换为int
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255, 3))

# 绘制最大矩形
x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (x+w, y+h),(255,0,0))

cv2.imshow('result', img)

cv2.waitKey(0)
