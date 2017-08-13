"""
问题描述：构造一个特殊的栈，要求
1）使之pop()、push()和getMin() (求最小值) 的操作的时间复杂度都为O(1)
2）可以使用现成的栈类型

思路：使用两个栈，一个栈保存所有数据，一个栈保存最小数据集
"""


class MyStack:
    def __init__(self):
        self.datastack = list()
        self.minstack = list()

    def push(self, value):
        length = len(self.minstack)
        if length == 0:
            self.minstack.append(value)
        else:
            if value <= self.minstack[-1]:
                self.minstack.append(value)

        self.datastack.append(value)

    def pop(self):
        if len(self.datastack) == 0:
            raise RuntimeError('the stack is empty')
        i = self.datastack.pop()
        if i == self.get_min():
            self.minstack.pop()
        return i

    def get_min(self):
        if len(self.datastack) == 0:
            raise RuntimeError('the stack is empty')
        return self.minstack[-1]


if __name__ == '__main__':
    stack = MyStack()
    stack.push(3)
    print(stack.get_min())
    stack.push(4)
    print(stack.get_min())
    stack.push(1)
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())