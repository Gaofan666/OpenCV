import cv2

im = cv2.imread('../img/自适应.png')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 转为灰度图
cv2.imshow('im', im)

# 二值化  返回阈值和二值化后的图像
im_bin = cv2.adaptiveThreshold(im,
                               255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # 高斯
                               cv2.THRESH_BINARY,  # type
                               3, 0)  # 块大小为3*3  C=0
cv2.imshow('im_bin', im_bin)

im_bin_inv = cv2.adaptiveThreshold(im,
                                   255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # 高斯
                                   cv2.THRESH_BINARY_INV,  # type
                                   3, 0)  # 块大小为3*3  C=0

cv2.imshow('im_bin_inv', im_bin_inv)

cv2.waitKey()
cv2.destroyAllWindows()
