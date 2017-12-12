"""
问题描述：给定一个链表的头结点head和一个整数num,请实现函数将值为num的节点
全部删除。例如，链表为
1->2->3->4->None,num=3 链表调整后为1->2->4->None
"""

from linkedlist.toolcls import Node, PrintMixin


class RemoveAssignedNode(PrintMixin):
    @classmethod
    def remove_node(cls, head, num):
        if head is None:
            return head

        pre = None
        cur = head

        new_head = head

        while cur is not None:
            next = cur.next
            if cur.value == num:
                if pre is not None:
                    pre.next = next
                else:
                    new_head = cur.next
                    cur.next = None
                    del cur
            else:
                pre = cur
            cur = next

        return new_head


if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(4)

    RemoveAssignedNode.print_list(RemoveAssignedNode.remove_node(node, 2))