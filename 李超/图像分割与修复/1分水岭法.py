import cv2
import numpy as np
import matplotlib.pyplot as mp

img = cv2.imread('../img/water_coins.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 获取背景
# 1. 二值化  , 这里的阈值设置0，其实是用到了OTSU自适应阈值，不需要我们自己设置
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 得到背景为黑色，硬币为白色的图
cv2.imshow('thresh', thresh)
# 2. 形态学获取背景
kernel = np.ones((3, 3), np.uint8)
# 开运算去除噪点
open_ = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 膨胀  得到背景
bg = cv2.dilate(open_, kernel, iterations=1)
cv2.imshow('bg', bg)

# 获取前景物体
dist = cv2.distanceTransform(open_, cv2.DIST_L2, 5)
# fg 前景
ret1, fg = cv2.threshold(dist, 0.7 * dist.max(), 255, cv2.THRESH_BINARY)
cv2.imshow('fg', fg)

# mp.imshow(dist, cmap='gray')  # 使用matplotlib显示出梯度
# mp.show()
# exit()

# 获取未知区域
fg = np.uint8(fg)
unknow = cv2.subtract(bg, fg)
cv2.imshow('unknow', unknow)

# 创建marker
# 创建连通域
ret2,marker = cv2.connectedComponents(fg)
# marker = np.uint8(marker)
# cv2.imshow('marker',marker)

marker = marker + 1  # 将所有的背景用1表示，前景255+1没什么影响
marker[unknow==255] = 0  # 设置未知区域的值为0

#进行图像分割
result = cv2.watershed(img , marker)

img[result == -1] = [0,0,255]
cv2.imshow('img',img)

cv2.waitKey(0)
