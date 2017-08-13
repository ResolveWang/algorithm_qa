"""
问题描述：编写一个类，用两个栈实现一个队列，要求:
支持队列的基本操作，add、poll和peek

思路：使用两个栈模拟队列操作
"""


class StackQueue:
    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def add(self, value):
        self.stack_in.append(value)

    def poll(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                raise RuntimeError('the queue is empty')
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                raise RuntimeError('the queue is empty')
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

if __name__ == '__main__':
    queue = StackQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.peek())
    print(queue.poll())
    print(queue.peek())
    print(queue.poll())
    print(queue.peek())
    print(queue.poll())
