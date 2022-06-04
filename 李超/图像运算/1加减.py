import cv2
import numpy as np

img1 = cv2.imread('../img/ex01.jpg')

# 图的加法运算就是矩阵的加法运算,因此加法运算的两张图必须相等

print(img1.shape)

img2 = np.ones((676, 1202, 3), np.uint8) * 100

# re = cv2.add(img1, img2)
re = cv2.subtract(img1, img2)

cv2.imshow('img1',img1)
cv2.imshow('result', re)

cv2.waitKey(0)