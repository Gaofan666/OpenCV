import cv2
import numpy as np

img = cv2.imread('../img/双边.png')

dst = cv2.bilateralFilter(img,7,50,50)

cv2.imshow('img',img)
cv2.imshow('dst',dst)


cv2.waitKey(0)