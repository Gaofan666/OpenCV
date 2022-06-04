import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 绘制文本
cv2.putText(img,"Hello world!",(10,240),1,5,(0,0,255),2)

cv2.imshow('img', img)
cv2.waitKey()
