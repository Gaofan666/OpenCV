import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
# 灰度化才能进行角点检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
# 计算关键点和描述子
kp,des = orb.detectAndCompute(gray,None)
print(des)

cv2.drawKeypoints(gray,kp,img)

cv2.imshow('ORB', img)

cv2.waitKey(0)
