import cv2
import numpy as np

# 创建一个黑色的图像
img = np.zeros((480, 640, 3), np.uint8)

# 图像分割
b, g, r = cv2.split(img)

# 修改b通道
b[10:100, 10:100] = 255
# 修改g通道
g[10:100, 10:100] = 255
cv2.imshow('b', b)
cv2.imshow('g', g)

# 合并b,g,r通道
img2 = cv2.merge((b, g,r))

cv2.imshow('img', img)
cv2.imshow('img2',img2)

cv2.waitKey()
