"""
问题描述：给定两个有序链表的头指针head1和head2,打印两个
链表的公共部分(即链表节点的值相同的部分)

思路：由于链表有序，所以可以比较head1和head2的值进行判断
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class PublicPart:
    @classmethod
    def get_public_part(cls, head1, head2):
        if head1 is None or head2 is None:
            return

        if head1.value == head2.value:
            print(head1.value, end=' ')
            cls.get_public_part(head1.next, head2.next)
        elif head1.value > head2.value:
            cls.get_public_part(head1, head2.next)
        elif head1.value < head2.value:
            cls.get_public_part(head1.next, head2)

if __name__ == '__main__':
    cur_head1 = Node(2)
    cur_head1.next = Node(3)
    cur_head1.next.next = Node(5)
    cur_head1.next.next.next = Node(6)

    cur_head2 = Node(1)
    cur_head2.next = Node(2)
    cur_head2.next.next = Node(5)
    cur_head2.next.next.next = Node(7)
    cur_head2.next.next.next.next = Node(8)

    PublicPart.get_public_part(cur_head1, cur_head2)