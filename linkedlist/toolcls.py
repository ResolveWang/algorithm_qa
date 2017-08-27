class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class PrintMixin:
    @staticmethod
    def print_list(head):
        while head is not None:
            print(head.value, end=' ')
            head = head.next
        print()

    @staticmethod
    def print_list_rand(head):
        while head is not None:
            if head.rand is None:
                print('-', end=' ')
            else:
                print(head.rand.value, end=' ')
            head = head.next
        print()
