"""
linklist  例如 : a=1 b=(2,a) c=(3,b)
功能：实现单链表的构建和功能操作
重点代码
"""


# 创建节点类
class Node:
    """
    思路：将自定义的类视为节点的生成类，实例对象中包含数据部分和只想下一个节点的next
    """

    def __init__(self, val, next=None):
        self.val = val  # 存储有用的数据
        self.next = next  # 寻找下一个节点关系


class LinkList:
    """
    思路：单链表类，生成对象后可以进行增删改查操作
          具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)  # 头节点是Node实例，有next

    def init_list(self, list_):  # 将列表中的元素-->链表
        p = self.head  # head不能动，就创建一个p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:  # 只要p的value不是None,一直打印
            print(p.val)
            p = p.next

    # 判断链表是否为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部增加节点 (效率低)
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        node = Node(val)  # 待插入的节点
        node.next = self.head.next  # 先把该节点和第一个节点连接起来
        self.head.next = node  # 再将头节点和该节点相连 ，顺序不可颠倒，如果直接断开头节点，链表会消失

    # 指定插入位置
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is Node:  # 超出链表范围，跳出循环，直接在尾部插入
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def delete(self, x):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next is not Node and p.next.val != x:  # and前后语句不可颠倒，应该先判断有没有下一个节点，再判断下一个节点的值
            p = p.next
        if p.next is Node:  # 如果没有找到该节点
            raise ValueError("x not in linklist")
        else:  # 那就是找到节点了
            p.next = p.next.next

    # 获取某个索引的值
    def get_index(self, index):
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("linklist index out of range")
            p = p.next
        return p.val

    @classmethod  # 将l2合并到l1中  类方法
    def merge(cls, l1, l2):
        p = l1.head
        q = l2.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                p = p.next
                q = tmp
        p.next = q
        return l1


if __name__ == '__main__':
    # l = LinkList()
    # list01 = [1, 2, 3, 4, 5]
    # l.init_list(list01)
    # l.show()
    # print(l.get_index(2))
    l1 = LinkList()
    l2 = LinkList()
    l1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
    l2.init_list([2, 3, 4, 9, 16, 17, 20])
    LinkList.merge(l1, l2)
    l1.show()
