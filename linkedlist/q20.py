"""
问题描述：给定一个单链表的头部节点head，链表长度为N，如果N为偶数，那么前N/2个节点算作左
半区，后N/2个节点算作右半区；如果N为奇数，那么前N/2个节点算作左半区，后N/2+1个节点算作
是右半区。左半区从左到右依次记作L1->L2->...,右半区从左到右依次记作R1->R2->...，请将
单链表调整成L1->R1->L2->R2...的形式
例如：
1->None,调整为1->None
1->2->None,调整为1->2->None
1->2->3->None,调整为1->2->3->None
1->2->3->4->None,调整为1->3->2->4->None
1->2->3->4->5->None,调整为1->3->2->4->5->None
1->2->3->4->5->6->None,调整为1->4->2->5->3->6->None
"""

from linkedlist.toolcls import Node, PrintMixin


class RefactorList(PrintMixin):
    @classmethod
    def refactor(cls, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        slow = head
        fast = head

        while slow is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is None or fast is None:
                break

        cur = head
        left_end = slow
        while cur != left_end:
            pre_right = slow
            left_next = cur.next
            right_next = slow.next

            cur.next = slow
            slow.next = left_next

            pre = cur
            cur = left_next
            slow = right_next
        pre.next = pre_right
        pre_right.next = slow
        return head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    RefactorList.print_list(RefactorList.refactor(head))

