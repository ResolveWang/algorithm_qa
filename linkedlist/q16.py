"""
问题描述：给定一个无序单链表的头结点head，实现单链表的选择排序
要求：额外空间复杂度为O(1)

思路：选择排序是从未排序的部分找到最小值，放到排好序部分的末尾
(区分选择和冒泡排序，冒泡是比较并交换，而选择是移动指针，每次指
针都是指向最小值，一趟过程后把当前指针指向的值放到排好序的尾部)
"""

from linkedlist.toolcls import Node, PrintMixin


class SortList(PrintMixin):
    @classmethod
    def sort_list(cls, head):
        cur = head
        new_head = cls.get_head(cur)
        cur = new_head
        temp = new_head
        while cur is not None:
            cur = cls.get_head(cur.next)
            temp.next = cur
            temp = cur
        return new_head

    @classmethod
    def get_head(cls, head):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head

        little_pre = None
        little = head

        while cur is not None:
            if cur.value < little.value:
                little_pre = pre
                little = cur
            pre = cur
            cur = cur.next

        if little != head:
            little_pre.next = little.next
            little.next = head
        return little


if __name__ == '__main__':
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)
    head = SortList.sort_list(head)
    SortList.sort_list(head)
    SortList.print_list(head)

    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(2)
    head = SortList.sort_list(head)
    SortList.print_list(head)
