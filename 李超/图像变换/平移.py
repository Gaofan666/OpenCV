import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 向右平移100个点
M = np.float32([[1, 0, 100], [0, 1, 0]])
h,w,c = img.shape
img1 = cv2.warpAffine(img,M,(w,h))

cv2.imshow('img', img)
cv2.imshow('img1', img1)

cv2.waitKey(0)
