import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)

dst = cv2.GaussianBlur(img,(5,5),sigmaX=1)
dst10 = cv2.GaussianBlur(img,(5,5),sigmaX=10)
dst100 = cv2.GaussianBlur(img,(5,5),sigmaX=100)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst10',dst10)
cv2.imshow('dst100',dst100)

cv2.waitKey(0)