import cv2
import numpy as np

img = cv2.imread('../img/7.png')
cv2.imshow('img', img)

# 膨胀
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

im1 = cv2.dilate(img, kernel1, iterations=2)  # 迭代次数
im2 = cv2.dilate(img, kernel2, iterations=2)  # 迭代次数
im3 = cv2.dilate(img, kernel3, iterations=2)  # 迭代次数

cv2.imshow('RECT', im1)
cv2.imshow('ELLIPSE', im2)
cv2.imshow('CROSS', im3)

cv2.waitKey()
cv2.destroyAllWindows()
