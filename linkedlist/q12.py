"""
问题描述：给定一个单链表的头结点head，实现一个调整单链表的函数，使得每K个节点之间逆序，
如果最后不够k个节点一组，则不调整最后几个节点。
例如：k = 3时
链表：1->2->3->4->5->6->7->8->null
调整后:3->2->1->6->5->4->7->8->null,7、8不调整，因为不够一组
"""


from linkedlist.toolcls import Node, PrintMixin


class ReversePartList(PrintMixin):
    @classmethod
    def reverse_part(cls, head, k):
        if head is None or k < 1:
            return head

        cur = head
        count = 0
        temp_stack = list()

        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        cur = head

        new_head = None
        circle_count = 0
        new_pre_node = None
        while cur is not None:
            count += 1
            temp_stack.append(cur)
            next = cur.next
            if count == k:
                pre_node = None
                first_node = None
                circle_count += 1
                while count > 0:
                    temp_node = temp_stack.pop(0)
                    if count == k:
                        first_node = temp_node
                    if circle_count == 1 and count == 1:
                        new_head = temp_node
                    temp_node.next = pre_node
                    if new_pre_node is not None and count == 1:
                        new_pre_node.next = temp_node
                    pre_node = temp_node
                    count -= 1
                new_pre_node = first_node
            cur = next
        if len(temp_stack) > 0:
            temp_node = temp_stack.pop(0)
            if new_pre_node is not None:
                new_pre_node.next = temp_node
            else:
                return temp_node

        return new_head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    k = 3
    ReversePartList.print_list(ReversePartList.reverse_part(head, k))



