import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)

dst = cv2.blur(img,(5,5))
cv2.imshow('img',img)
cv2.imshow('dst',dst)

cv2.waitKey(0)
