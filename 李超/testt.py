import cv2
img = cv2.imread('img/cat.jpg')
cv2.imshow('cat',img)

while True:
    key = cv2.waitKey(1)
    if key>0:
        print(key)