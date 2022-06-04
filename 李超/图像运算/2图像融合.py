import cv2
import numpy as np
cv2.namedWindow('result',cv2.WINDOW_NORMAL)
cv2.namedWindow('img1',cv2.WINDOW_NORMAL)
cv2.namedWindow('img2',cv2.WINDOW_NORMAL)

img1 = cv2.imread('../img/ex01.jpg')
img2 = cv2.imread('../img/ex03.jpg')

# 只有两张图的属性一致，才可以融合
print(img1.shape)
print(img2.shape)

result = cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('result',result)

cv2.waitKey(0)