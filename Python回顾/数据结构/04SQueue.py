"""
队列的顺序存储
思路分析：
1.基于列表完成数据存储
2.通过封装规定数据操作
3.先确定哪一端作队头，队尾
"""


# 自定义队列异常
class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems = []

    # 入队  列表尾部定义为队尾
    def enqueue(self, val):
        self._elems.append(val)

    # 出队
    def dequeue(self):
        if not self._elems:  # 代码简洁
            raise QueueError(" queue is empty")
        return self._elems.pop(0)  # 列表第一个元素为队头

    # 判断队列是否为空
    def is_empty(self):
        return self._elems == []


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())
