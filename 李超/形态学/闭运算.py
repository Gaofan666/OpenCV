# 先腐蚀，后膨胀
import cv2
import numpy as np

# 读取原图
im = cv2.imread('../img/9.png')

# 闭运算
k = np.ones((10, 10), np.uint8)  # 计算核的类型uint8
# k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))  # 获取卷积核
r1 = cv2.morphologyEx(im, cv2.MORPH_CLOSE, k)

cv2.imshow('im', im)
cv2.imshow('r1', r1)

cv2.waitKey()
cv2.destroyAllWindows()