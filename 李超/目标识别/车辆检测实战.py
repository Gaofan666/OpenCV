import cv2
import numpy as np

# 加载视频
cap = cv2.VideoCapture('../img/video.mp4')

# 背景去除
bgsubmog = cv2.createBackgroundSubtractorMOG2()

# 创建腐蚀膨胀的卷积核
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# 设置最小宽高阈值
min_w, min_h = 90, 90
# 创建一个列表存放车辆轮廓中心点
cars = []
car_n = 0  # 车辆的个数
# 检测线的高   视频的尺寸为1280*720
line_height = 550
# 线的偏移
line_offset = 6


# 定义函数，计算中心点
def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


while True:
    ret, frame = cap.read()
    if ret:
        # 灰度化
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 由于一些树叶也会动，形成噪点，所以进行去噪
        blur = cv2.GaussianBlur(frame, (9, 9), 5)  # 9*9可以自己设置 3*3  5*5 7*7.。。
        mask = bgsubmog.apply(blur)  # 去除背景
        # 腐蚀
        erode = cv2.erode(mask, k)
        # 腐蚀之后变小了，要膨胀
        dilate = cv2.dilate(erode, k, iterations=2)
        # 闭操作，去掉物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, k)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, k)
        # 查找轮廓
        contours, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 每一帧都要画线
        cv2.line(frame, (0, line_height), (1280, line_height), (0, 255, 0), 2)
        for (i, c) in enumerate(contours):  # 拿到索引和边界
            (x, y, w, h) = cv2.boundingRect(c)  # 绘制矩形
            if w >= min_w and h >= min_h:  # 如果是车辆，绘制轮廓
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))
                # 存取车的轮廓的中心点，如果中心点过线，代表有车经过
                cpoint = center(x, y, w, h)  # 计算中心点
                cars.append(cpoint)
                for (x, y) in cars:
                    # 如果车在线的上下偏移量之间，表示有车辆经过
                    if (y > line_height - line_offset) and (y < line_height + line_offset):
                        car_n += 1  # 车的数量+1
                        cars.remove((x, y))
                        print(car_n)
            else:  # 如果不是车辆，跳过
                continue
        # 显示车辆的统计信息
        cv2.putText(frame, 'Cars Count:' + str(car_n), (500, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

        cv2.imshow('video', frame)
    key = cv2.waitKey(33)
    if key == 113:  # 按‘q'退出
        break

cap.release()
cv2.destroyAllWindows()
