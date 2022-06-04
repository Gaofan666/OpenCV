import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
print(img.shape)  #676 1202 3
# 缩放成指定大小
new = cv2.resize(img,(400,400))
# 按fx,fy缩放：  三次插值
new2 = cv2.resize(img,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.imshow('new2',new2)

cv2.waitKey(0)