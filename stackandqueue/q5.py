"""
问题描述：一个栈中元素的类型为整型，现在想将该栈从顶到底按从大到小的顺序排序，只许
额外申请一个栈。除此之外，可以申请新的变量，但不能申请额外的数据结构。如何完成排序？

思路：将要排序的栈记为stack，申请的辅助栈记为help。在stack上执行pop操作，弹出的
元素记为cur.
1)如果cur小于或等于help的栈顶元素，则将cur直接压入help
2)如果cur大于help的栈顶元素，则将help的元素逐一弹出，逐一压入stack，直到cur小于
或等于help的栈顶元素，再将cur压入help
3)将help的所有元素压入stack
"""


class SortedStack:
    def __init__(self):
        self.stack = list()
        self.help = list()

    def push(self, value):
        self.stack.append(value)

    def sort_stack(self):
        if len(self.stack) == 0:
            return self.stack
        while len(self.stack) > 0:
            cur = self.stack.pop()
            while len(self.help) > 0 and cur > self.help[-1]:
                help_top = self.help.pop()
                self.stack.append(help_top)
            self.help.append(cur)

        while len(self.help) > 0:
            self.stack.append(self.help.pop())

if __name__ == '__main__':
    sortStack = SortedStack()
    sortStack.push(3)
    sortStack.push(1)
    sortStack.push(6)
    sortStack.push(2)
    sortStack.push(5)
    sortStack.push(4)

    sortStack.sort_stack()
    print(sortStack.stack)