"""
问题描述：给定一个单链表的头结点head，实现一个调整单链表的函数，使得每K个节点之间逆序，
如果最后不够k个节点一组，则不调整最后几个节点。
例如：k = 3时
链表：1->2->3->4->5->6->7->8->None
调整后:3->2->1->6->5->4->7->8->None,7、8不调整，因为不够一组

思路：
1）使用辅助栈或者队列来做n*k个节点的倒置
2）直接使用有限（四个）变量来解决该问题，left表示每k个节点的前一个，start表示每k个节点
的第一个，end表示每k个节点的最后一个，right表示每k个节点的最后一个的下一个。在翻转之前，
有关系：left.next = start  end.next = right。可利用该关系解决。注意边界条件
"""


from linkedlist.toolcls import Node, PrintMixin


class ReversePartList(PrintMixin):
    @classmethod
    def reverse_part(cls, head, k):
        if head is None or k < 1:
            return head

        cur = head
        count = 0
        # 辅助队列
        temp_stack = list()

        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        cur = head
        # 倒置后的头结点
        new_head = None
        # 当前出现了几个 "k节点" 了
        circle_count = 0
        # 每k个节点的尾节点倒置后的前一个节点
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



