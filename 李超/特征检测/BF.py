import cv2
import numpy as np

img1 = cv2.imread('../img/opencv_search.png')
img2 = cv2.imread('../img/opencv_orig.png')
# 灰度化才能进行角点检测
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
# 计算关键点和描述子
kp1,des1 = sift.detectAndCompute(gray1,None)
kp2,des2 = sift.detectAndCompute(gray2,None)

bf = cv2.BFMatcher(cv2.NORM_L1)
match = bf.match(des1,des2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,match,None)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
