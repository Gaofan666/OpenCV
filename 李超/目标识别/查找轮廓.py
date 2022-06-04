import cv2
import numpy as np

img = cv2.imread('../img/contours1.jpeg')
# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('bin',bin)
# 轮廓查找
contours,hierarchy = cv2.findContours(bin,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)  # 打印出找到的角点

# 绘制轮廓,可以在bin上绘制，也可以在img绘制,需要注意的是img是三通道。bin是单通道
cv2.drawContours(img,contours,-1,(0,0,255),2)
cv2.imshow('contours',img)

# 计算面积
area = cv2.contourArea(contours[0])
print('area = %d'% area)

# 计算周长
len = cv2.arcLength(contours[0],True)
print('len = %d'%len)

cv2.waitKey(0)
