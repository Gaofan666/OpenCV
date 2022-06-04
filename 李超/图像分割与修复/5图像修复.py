import cv2
import numpy as np

img = cv2.imread('../img/inpaint.png')
mask = cv2.imread('../img/inpaint_mask.png', 0)
cv2.imshow('mask',mask)

dst = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)

cv2.imshow('dst', dst)
cv2.imshow('img', img)

cv2.waitKey()

