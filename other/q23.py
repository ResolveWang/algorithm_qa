"""
问题描述:已知一个消息流会不断吐出整数1~N，但不一定按照顺序吐出。如果上次
打印的数为i,那么当i+1出现时,请打印i+1及其以后接收过的并且连续的所有数,直
到１~N全部接收并打印完，请设计这种接收并且打印的结构.

要求:
消息流最终会吐出全部的1~N，当然最终也会打印完所有的1~N,要求接收和打印1~N
的整个过程,时间复杂度为O(N)
"""


class Node:
    def __init__(self, num):
        self.num = num
        self.next = None


class MessageBox:
    def __init__(self):
        self.head_map = dict()
        self.tail_map = dict()
        self.last_num = 0

    def recevie(self, n):
        if n < 1:
            return
        new_node = Node(n)
        self.head_map[n] = new_node
        self.tail_map[n] = new_node

        if self.tail_map.get(n-1):
            old_tail = self.tail_map.get(n-1)
            old_tail.next = new_node
            self.tail_map.pop(n-1)
            self.head_map.pop(n)

        if self.head_map.get(n+1):
            old_head = self.head_map.get(n+1)
            new_node.next = old_head
            self.head_map.pop(n+1)
            self.tail_map.pop(n)

        if self.head_map.get(self.last_num+1):
            self.print_in_order(self.last_num+1)

    def print_in_order(self, n):
        head = self.head_map.pop(n)
        print(head.num, end=' ')
        self.last_num = head.num
        while head.next is not None:
            head = head.next
            print(head.num, end=' ')
            self.last_num = head.num
        self.tail_map.pop(self.last_num)
        print()


if __name__ == '__main__':
    box = MessageBox()
    box.recevie(2)
    box.recevie(1)
    box.recevie(4)
    box.recevie(5)
    box.recevie(7)
    box.recevie(8)
    box.recevie(6)
    box.recevie(3)
    box.recevie(9)
    box.recevie(10)
    box.recevie(12)
    box.recevie(13)
    box.recevie(11)