"""
问题描述：给定一个单链表的头结点head,以及两个整数from和to，在单链表上
把第from个节点到第to个节点这一部分进行反转。
例如：
1->2->3->4->5->None, from=2, to=4
调整结果为：1->4->3->2->5->None

再如：
1->2->3->None, from=1, to=3
调整结果为:
3->2->1->None

要求：
1.如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
2.如果不满足1<=from<=to<=N，则不用调整
"""

from linkedlist.toolcls import Node,PrintMixin


class RevertPart(PrintMixin):
    @classmethod
    def revert_part_of_linked_list(cls, head, list_from, list_to):
        if list_from >= list_to or list_from < 1 or head is None:
            return head

        fpre = None
        fnext = None
        length = 0

        node1 = head
        while node1 is not None:
            length += 1
            if length == list_from - 1:
                fpre = node1
            if length == list_to + 1:
                fnext = node1
            node1 = node1.next

        if length < list_to - list_from:
            return head

        if fpre is None:
            node1 = head
        else:
            node1 = fpre.next

        node2 = node1.next
        node1.next = fnext

        while node2 != fnext:
            next = node2.next
            node2.next = node1
            node1 = node2
            node2 = next

        if fpre is None:
            return node1

        fpre.next = node1
        return head

if __name__ == '__main__':
    head = None
    head = RevertPart.revert_part_of_linked_list(head, 1, 1)
    RevertPart.print_list(head)

    head = None
    head = RevertPart.revert_part_of_linked_list(head, 1, 1)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head = RevertPart.revert_part_of_linked_list(head, 1, 2)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = RevertPart.revert_part_of_linked_list(head, 1, 2)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = RevertPart.revert_part_of_linked_list(head, 2, 3)
    RevertPart.print_list(head)