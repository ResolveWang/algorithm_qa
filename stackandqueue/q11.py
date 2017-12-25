"""
问题描述：用数组结构实现大小固定的队列和栈。
"""


class Stack:
    def __init__(self, n):
        self.arr = [0 for _ in range(n)]
        self.index = -1

    def peek(self):
        if self.index == -1:
            return

        return self.arr[self.index]

    def push(self, n):
        if self.index == len(self.arr) - 1:
            raise Exception('the stack is full')

        self.index += 1
        self.arr[self.index] = n

    def pop(self):
        if self.index == -1:
            raise Exception('the stack is empty')

        tmp = self.arr[self.index]
        self.arr[self.index] = 0
        self.index -= 1
        return tmp


class Queue:
    def __init__(self, n):
        self.size = 0
        self.start = 0
        self.end = 0
        self.arr = [0 for _ in range(n)]

    def peek(self):
        pass

    def push(self, n):
        if self.size == len(self.arr):
            raise Exception('the queue is full')

        self.size += 1
        self.arr[self.end] = n
        if self.end + 1 == len(self.arr):
            self.end = 0
        else:
            self.end += 1

    def poll(self):
        if self.size == 0:
            raise Exception('the queue is empty')

        self.size -= 1
        tmp = self.arr[self.start]
        self.arr[self.start] = 0
        if self.start + 1 == len(self.arr):
            self.start = 0
        else:
            self.start += 1

        return tmp


if __name__ == '__main__':
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    # stack.push(6)
    print(stack.arr)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())

    queue = Queue(5)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    # queue.push(6)
    print(queue.arr)
    print(queue.poll())
    print(queue.poll())
    print(queue.poll())
    print(queue.poll())
    print(queue.poll())
    # print(queue.poll())


