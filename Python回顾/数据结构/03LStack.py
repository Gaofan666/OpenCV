"""
链式栈
重点代码
思路：1.源于链表结构
      2.封装栈的操作方法（入栈，出栈，栈空，栈顶元素）
      3.链表的开头作为栈顶 ？ （不用每次遍历）
"""


# 自定义异常
class StackError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        self._top = Node(val, self._top)  # 代码简洁

    def pop(self):
        if self._top is Node:
            raise StackError("stack is empty")
        value = self._top.val  # 先取到栈顶的值
        self._top = self._top.next  # 再使top指向下一个节点
        return value

    def top(self):
        if self._top is Node:
            raise StackError("stack is empty")
        return self._top.val


if __name__ == '__main__':
   ls = LStack()
   ls.push(1)
   ls.push(2)
   ls.push(3)
   print(ls.pop())