import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')

blockSize = 2
ksize = 3
k = 0.04

# 灰度化才能进行角点检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Harris角点检测
dst = cv2.cornerHarris(gray, blockSize, ksize, k)

#角点展示
img[dst > 0.01*dst.max()] = [0,0,255]

cv2.imshow('harris',img)

cv2.waitKey(0)
