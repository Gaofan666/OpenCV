import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 对x方向求导
dst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
