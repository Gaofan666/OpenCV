import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)

# 对x方向求导
dstx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

# 对y求导
dsty = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#合并
dst = dstx + dsty

cv2.imshow('img',img)
cv2.imshow('dstx',dstx)
cv2.imshow('dsty',dsty)
cv2.imshow('dst',dst)

cv2.waitKey(0)