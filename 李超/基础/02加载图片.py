import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('../img/ex01.jpg')
cv2.imshow('img', img)
while True:
    key = cv2.waitKey(0)
    print('key=',key)
    print('type=',type(key))
    if key == 113:  # 按键q
        print("退出")
        break
    elif key == 120:  # 按键x
        print("保存")
        cv2.imwrite('../img/123.png', img)
    else:
        print('other')
cv2.destroyAllWindows()