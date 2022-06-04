import cv2

img = cv2.imread('../img/ex03.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)

img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img2 = cv2.rotate(img, cv2.ROTATE_180)
img3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
