import cv2
import numpy as np

img = cv2.imread('../img/5.png')
cv2.imshow('img', img)

# 腐蚀
kernel = np.ones((3, 3), np.uint8)  # 计算腐蚀核
im_erode = cv2.erode(img, kernel, iterations=10)  # 迭代次数
cv2.imshow('im_erode', im_erode)

cv2.waitKey()
cv2.destroyAllWindows()
