import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img2 = cv2.imread('../img/ex01.jpg')

# 非运算
# img2 = cv2.bitwise_not(img)

# 与运算
# img3 = cv2.bitwise_and(img,img2)

#或
# img3 = cv2.bitwise_or(img,img2)

#异或
img3 = cv2.bitwise_xor(img,img2)

# cv2.imshow('img',img)
cv2.imshow('img3',img3)

cv2.waitKey(0)