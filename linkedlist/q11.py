"""
问题描述：单链表可能有环，也可能无环。给定两个单链表的头结点head1和head2,
这两个链表可能相交，也可能不相交。请实现一个函数，如果两个链表相交，请返回相
交的第一个节点，如果不相交，返回None即可。

要求：如果链表1的长度为N，链表2的长度为M，时间复杂度请达到O(M+N),额外空间复
杂读请达到O(1)

思路：
1）使用快慢指针判断是否有环，有环可以通过快慢指针求出环和非环部分的交点
"""


from linkedlist.toolcls import Node


class PublicNodeGetTool:
    @classmethod
    def get_first_node_of_circle(cls, head):
        fast = head
        slow = head

        while fast is not None:
            if fast.next is not None:
                fast = fast.next.next
            else:
                return None
            slow = slow.next

            if slow == fast:
                fast = head
                break

        if fast is None:
            return None

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

    @classmethod
    def get_public_node(cls, head1, head2):
        node1 = cls.get_first_node_of_circle(head1)
        node2 = cls.get_first_node_of_circle(head2)
        if node1 is None and node2 is None:
            return cls.get_public_node_of_list(head1, head2)

        elif node1 is not None and node2 is not None:
            length1 = 1
            length2 = 1
            cur1 = head1
            cur2 = head2

            while cur1 != node1:
                length1 += 1
                cur1 = cur1.next

            while cur2 != node2:
                length2 += 1
                cur2 = cur2.next

            if node1 != node2:
                if length1 > length2:
                    return node2
                else:
                    return node1
            else:
                temp = length1 - length2
                cur1 = head1
                cur2 = head2

                if temp > 0:
                    while temp > 0:
                        cur1 = cur1.next
                        temp -= 1
                    while cur1 is not None:
                        if cur1 == cur2:
                            return cur1
                        else:
                            cur1 = cur1.next
                            cur2 = cur2.next
                elif temp == 0:
                    while length1 > 0:
                        if cur1 == cur2:
                            return cur1
                        else:
                            cur1 = cur1.next
                            cur2 = cur2.next
                            length1 -= 1
                else:
                    while temp < 0:
                        cur2 = cur2.next
                        temp += 1
                    while cur2 is not None:
                        if cur1 == cur2:
                            return cur1
                        else:
                            cur1 = cur1.next
                            cur2 = cur2.next
        else:
            return None

    @classmethod
    def get_public_node_of_list(cls, head1, head2):
        pre1 = None
        pre2 = None
        length1 = 0
        length2 = 0

        cur1 = head1
        cur2 = head2

        while cur1 is not None or cur2 is not None:
            if cur1 is not None:
                pre1 = cur1
                cur1 = cur1.next
                length1 += 1

            if cur2 is not None:
                pre2 = cur2
                cur2 = cur2.next
                length2 += 1

        if pre1 is None or pre2 is None or pre1 != pre2:
            return None

        temp = length1 - length2
        cur1 = head1
        cur2 = head2

        if temp > 0:
            while temp > 0:
                cur1 = cur1.next
                temp -= 1
            while cur1 is not None:
                if cur1 == cur2:
                    return cur1
                else:
                    cur1 = cur1.next
                    cur2 = cur2.next
        elif temp == 0:
            while length1 > 0:
                if cur1 == cur2:
                    return cur1
                else:
                    cur1 = cur1.next
                    cur2 = cur2.next
                    length1 -= 1
            return None
        else:
            while temp < 0:
                cur2 = cur2.next
                temp += 1
            while cur2 is not None:
                if cur1 == cur2:
                    return cur1
                else:
                    cur1 = cur1.next
                    cur2 = cur2.next


if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next
    print(PublicNodeGetTool.get_public_node(head1, head2).value)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next = head1.next.next.next

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next
    print(PublicNodeGetTool.get_public_node(head1, head2).value)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next
    print(PublicNodeGetTool.get_public_node(head1, head2).value)