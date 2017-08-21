"""
问题描述：分别实现反转单向链表和反转双向链表的函数

要求：如果链表为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
"""


from linkedlist.toolcls import PrintMixin, Node


class RevertList(PrintMixin):
    @classmethod
    def revert_linked_list(cls, head):
        pre = None
        next = None

        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre


if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    revert_node = RevertList.revert_linked_list(node)
    RevertList.print_list(revert_node)