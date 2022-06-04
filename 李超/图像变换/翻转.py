import cv2

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)

# 上下翻转
img1 = cv2.flip(img, 0)

# 左右翻转
img2 = cv2.flip(img, 1)

# 上下加左右
img3 = cv2.flip(img, -1)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
