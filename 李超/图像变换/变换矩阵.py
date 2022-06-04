import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')
h, w, c = img.shape

# 获取变换矩阵M
# M = cv2.getRotationMatrix2D((w / 2, h / 2), 60, 1.0)

src = np.float32([[400,300],[800,300],[400,1000]])
dst = np.float32([[200,400],[600,500],[150,1100]])
# 第二种获取仿射变化图片的方法:通过变换前后点的坐标
M = cv2.getAffineTransform(src,dst)

img1 = cv2.warpAffine(img, M, (w, h))

cv2.imshow('img', img)
cv2.imshow('img1', img1)

cv2.waitKey(0)
