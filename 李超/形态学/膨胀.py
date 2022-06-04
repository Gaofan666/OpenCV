import cv2
import numpy as np

img = cv2.imread('../img/7.png')
cv2.imshow('img', img)

# 腐蚀
kernel = np.ones((3, 3), np.uint8)  # 计算腐蚀核
img1 = cv2.dilate(img, kernel, iterations=10)  # 迭代次数
img2 = cv2.dilate(img, kernel, iterations=20)  # 迭代次数
img3 = cv2.dilate(img, kernel, iterations=50)  # 迭代次数

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()
