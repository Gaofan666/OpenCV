import cv2
import numpy as np
import pytesseract

# 第一步，创建Haar级联器
plate = cv2.CascadeClassifier('../img/haarcascades/haarcascade_russian_plate_number.xml')

# 第二步，导入图片
img = cv2.imread('../img/chinacar.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步，车牌定位
# 返回数组[[x,y,w,h]]
# 检测车牌位置
plate = plate.detectMultiScale(gray, 1.1, 3)
for (x, y, w, h) in plate:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 对车牌进行预处理
# 提取ROI
roi = gray[y:y + h, x:x + w]
# 二值化
ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 进行文字提取，lang是语言，中文加英文，中间用+号
# OCR引擎模式oem可选： 0：OriginalTesseract  1:神经网络LSTM  2：Tesseract+LSTM  3:默认什么可选选什么
text = pytesseract.image_to_string(roi , lang='chi_sim+eng',config='--psm 8 --oem 3')
print(text) # 5N555

cv2.imshow('img', img)
cv2.imshow('roi_bin',roi_bin)
cv2.waitKey(0)
