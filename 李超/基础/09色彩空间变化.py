import cv2


def callback(a):
    pass


cv2.namedWindow('color', cv2.WINDOW_NORMAL)

img = cv2.imread('../img/ex01.jpg')

# 定义一个颜色模式的列表，拖动滑块时，颜色空间从这里选
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY,
               cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces)-1, callback)

while True:
    index = cv2.getTrackbarPos('curcolor', 'color')
    # 颜色空间转换cv2.cvtColor
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(1)
    if key == 113:
        break
cv2.destroyAllWindows()
