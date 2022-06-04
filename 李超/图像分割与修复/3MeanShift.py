import cv2
import numpy as np

img = cv2.imread('../img/flower.png')

m_img = cv2.pyrMeanShiftFiltering(img, 20, 30)

canny = cv2.Canny(m_img, 150, 300)

contours, h = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('img', img)
cv2.imshow('m_img', m_img)
cv2.imshow('canny', canny)
cv2.drawContours(img, contours, -1, (0, 0, 255, 2))
cv2.imshow('result',img)

cv2.waitKey(0)
