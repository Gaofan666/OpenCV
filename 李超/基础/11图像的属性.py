import cv2
import numpy as np

img = cv2.imread('../img/ex01.jpg')

# shape属性包含三个信息，分别是高度，宽度，通道数
print('img.shape = ', img.shape)

# size属性表示图片占多大内存空间 高*宽*通道数
print('img.size = ', img.size)

# 图像中每个元素的位深
print('img.dtype = ', img.dtype)  # uint8  取值范围0-255
