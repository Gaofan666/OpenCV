class Wife:
    # 数据成员
    def __init__(self, name, sex):
        # 数据成员
        self.name = name
        self.sex = sex

        # 行为成员

    def play(self):
        print(self.name + "玩耍")


# 创建对象
w01 = Wife("莉莉", 22)  # 自动将对象地址传入方法
# 调用对象行为
w01.play()
