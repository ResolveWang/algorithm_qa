"""
问题描述：给定两个有序单链表的头结点head1和head2，请合并两个有序链表，合并后的链表依然
有序，并返回合并后链表的头结点。
例如：
0->2->3->7->None
1->3->5->7->9->None
合并后的链表为：0->1->2->3->3->5->7->7->9->None
"""

from linkedlist.toolcls import Node, PrintMixin


class MergeListTool(PrintMixin):
    @classmethod
    def merge(cls, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        cur1 = head1
        cur2 = head2

        while cur1 is not None and cur2 is not None:
            while cur1 is not None and cur1.value <= cur2.value:
                pre = cur1
                cur1 = cur1.next
            pre.next = cur2

            if cur1 is None:
                break

            while cur2 is not None and cur1.value > cur2.value:
                pre = cur2
                cur2 = cur2.next
            pre.next = cur1

            if cur2 is None:
                break

        if head1.value < head2.value:
            return head1
        else:
            return head2


if __name__ == '__main__':
    head1 = Node(0)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(7)

    head2 = Node(1)
    head2.next = Node(3)
    head2.next.next = Node(5)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(9)

    new_head = MergeListTool.merge(head1, head2)
    MergeListTool.print_list(new_head)