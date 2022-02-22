"""
链式队列
思路：1.基于链表构建队列模型
      2.链表的开端作为队头，结尾作为队尾
      3.单独定义队尾标记，避免每次插入数据遍历
      4.队头和队尾重叠认为队列为空
"""


# 自定义异常
class QueueError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear  # 头指针和尾指针相等时队列为空

    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next  # 别忘了把rear指针往后移动

    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("queue is empty")
        self.front = self.front.next  # front指针向后移动
        return self.front.val  # 返回front指向的节点的值，被front指向的节点相当于出队了


if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty(): #打印队列值
        print(lq.dequeue())
