import torch
from torch import nn
import matplotlib.pyplot as plt  # 绘画
import torch.nn.functional as F  # nn完成神经网络相关工作
from torch import optim  # 优化工具包
import torchvision
from utils import plot_image, plot_curve, one_hot
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# step1 load dataset
batch_size = 512
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data', train=True, download=False,  # 划分训练集，True如果没有数据集就进行下载
                               transform=torchvision.transforms.Compose(
                                   [torchvision.transforms.ToTensor(),  # array转化成Tensor格式
                                    torchvision.transforms.Normalize(  # 正则化
                                        (0.1307,), (0.3081,))
                                    ])),
    batch_size=batch_size, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data/', train=False, download=True,
                               transform=torchvision.transforms.Compose(
                                   [torchvision.transforms.ToTensor(),  # array转化成Tensor格式
                                    torchvision.transforms.Normalize(  # 正则化
                                        (0.1307,), (0.3081,))
                                    ])),
    batch_size=batch_size, shuffle=False)


# x, y = next(iter(train_loader))
# print(x.shape, y.shape, x.max())
# plot_image(x, y, 'image sample')


# 创建网络
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # xw+b
        self.fc1 = nn.Linear(28 * 28, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        # x: [b, 1, 28, 28]
        # h1 = relu(xw1+b1)
        x = F.relu(self.fc1(x))
        # h2 = relu(h1w2+b2)
        x = F.relu(self.fc2(x))
        # h3 = h2w3+b3
        x = self.fc3(x)

        return x


net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

train_loss = []

for epoch in range(3):
    for batch_idx, (x, y) in enumerate(train_loader):
        # x:[b,1,28,28] , y:[512]
        # [b,1,28,28] => [b,784]
        x = x.view(x.size(0), 28 * 28)
        # [b,10]
        out = net(x)
        y_onehot = one_hot(y)
        # loss=mse(out,y_onehot)
        loss = F.mse_loss(out, y_onehot)

        optimizer.zero_grad()  # 梯度清零
        loss.backward()  # 计算损失
        # w'= w - lr*grad
        optimizer.step()
        train_loss.append(loss.item())

        if batch_idx % 10 == 0:
            print(epoch, batch_idx, loss.item())

plot_curve(train_loss)

total_correct = 0
for x, y in test_loader:
    x = x.view(x.size(0), 28 * 28)
    out = net(x)
    # out:[b,10]  pred:[b]
    pred = out.argmax(dim=1)
    correct = pred.eq(y).sum().float().item()  # 预测对的总个数
    total_correct += correct

total_num = len(test_loader.dataset)  # 测试集的数量
acc = total_correct / total_num  # 准确率
print('test_acc:', acc)

x, y = next(iter(test_loader))
out = net(x.view(x.size(0), 28 * 28))
pred = out.argmax(dim=1)
plot_image(x, pred, 'test')
