import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
# 灰度化才能进行角点检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create() # 报错
# 计算关键点和描述子
kp,des = surf.detectAndCompute(gray,None)
print(des)

cv2.drawKeypoints(gray,kp,img)

cv2.imshow('SURF', img)

cv2.waitKey(0)
