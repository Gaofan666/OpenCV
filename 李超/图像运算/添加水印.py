import cv2
import numpy as np

img = cv2.imread('../img/ex03.jpg')

# 创建LOGO
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200, 1), np.uint8)  # 掩码

# 绘制LOGO
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

# 对mask按位求反，都变成 0
m = cv2.bitwise_not(mask)

# 选择图像的位置添加LOGO
roi = img[0:200, 0:200]

# 和m进行与操作,单通道可以直接与，多通道需要用mask
tmp = cv2.bitwise_and(roi, roi, mask=m)

# 叠加
dst = cv2.add(tmp,logo)

img[0:200,0:200] = dst  #加到图片里面

cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.imshow('m', m)
cv2.imshow('tmp', tmp)
cv2.imshow('dst', dst)
cv2.imshow('img', img)

cv2.waitKey(0)
