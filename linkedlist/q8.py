"""
问题描述：给定一个单向链表的头结点head，节点的值类型是整型，再给定一个
整数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于pivot
的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点，除
这个要求外，对调整后的节点顺序没有更多的要求

例如：链表 9->0->4->5->1,pivot=3
调整后的链表可以是1->0->4->9->5,也可以是0->1->9->5->4,中间部分都是
等于3的节点（本例中这个部分为空），右部分都是大于3的节点即可。对某部分内
部的节点顺序不作要求。

进阶：
在原问题的要求之上再增加两个要求：
1）在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左到右的顺
序与原链表中节点的先后次序一致,比如9->0->4->5->1,pivot=3，那么调整后
链表为0->1->9->5->4
2）如果链表的长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)
"""


from linkedlist.toolcls import Node,PrintMixin


class ListPartion(PrintMixin):
    @classmethod
    def strict_partion(cls, head, pivot):
        if head is None or head.next is None:
            return head

        left = None
        right = None
        pivot_node = None

        left_head = None
        right_head = None
        pivot_head = None

        temp = head

        while temp is not None:
            if temp.value < pivot:
                if left is None:
                    left = temp
                    left_head = left
                else:
                    left.next = temp
                    left = left.next
            elif temp.value == pivot:
                if pivot_node is None:
                    pivot_node = temp
                    pivot_head = temp
                else:
                    pivot_node.next = temp
                    pivot_node = pivot_node.next
            else:
                if right is None:
                    right = temp
                    right_head = temp
                else:
                    right.next = temp
                    right = right.next

            temp = temp.next

        if left_head is not None:
            if pivot_head is not None:
                left.next = pivot_head
                pivot_head.next = right_head
            else:
                left.next = right_head
            if right.next is not None:
                right.next = None
            return left_head

        else:
            if pivot_head is not None:
                pivot.next = right_head
                if right.next is not None:
                    right.next = None
                return pivot_head
            else:
                return right_head

if __name__ == '__main__':
    node = Node(9)
    node.next = Node(0)
    node.next.next = Node(4)
    node.next.next.next = Node(5)
    node.next.next.next.next = Node(1)

    partion_node = ListPartion.strict_partion(node, 4)
    ListPartion.print_list(partion_node)


