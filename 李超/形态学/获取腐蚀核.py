import cv2
import numpy as np

img = cv2.imread('../img/5.png')
cv2.imshow('img', img)

# 腐蚀
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(kernel1)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(kernel2)
kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print(kernel3)

im1 = cv2.erode(img, kernel1, iterations=2)  # 迭代次数
im2 = cv2.erode(img, kernel2, iterations=2)  # 迭代次数
im3 = cv2.erode(img, kernel3, iterations=2)  # 迭代次数

cv2.imshow('RECT', im1)
cv2.imshow('ELLIPSE', im2)
cv2.imshow('CROSS', im3)

cv2.waitKey()
cv2.destroyAllWindows()
