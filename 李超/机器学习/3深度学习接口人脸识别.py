import numpy as np
import argparse
import time
import cv2
from cv2 import dnn

# 1.导入模型，创建神经网络
config = '../img/model/bvlc_googlenet.prototxt'
model = '../img/model/bvlc_googlenet.caffemodel'
net = dnn.readNetFromCaffe(config, model)

# 2.读取图片，转为张量
img = cv2.imread('../img/smallcat.jpeg')
blob = dnn.blobFromImage(img,
                  1.0,  # 缩放因子
                  (224, 224),  # 模型要求的图片尺寸
                  (104, 117, 123))  # 模型定义的
# 3.将张量输入网络中，进行预测
net.setInput(blob)
r = net.forward()  # r是分类后的结果

# 读入类目
path = '../img/model/synset_words.txt'
classes = []
with open(path, 'rt') as f:
    classes = [x[x.find(" ") + 1:] for x in f]
# 每行的第一项进行倒序
ord = sorted(r[0], reverse=True)
# 对匹配最高的三项打印出来
z = list(range(3))
for i in range(0, 3):
    z[i] = np.where(r[0] == ord[i])[0][0]
    print('第', i + 1, '项，匹配：', classes[z[i]], end='')
    print('类所在行：', z[i] + 1, '可能性：', ord[i])
