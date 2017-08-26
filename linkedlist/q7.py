"""
问题描述：给定一个链表的头结点，请判断该链表是否为回文结构，例如：
1->2->1,返回true
1->2->2->1,返回true
15->6->15,返回true
1->2->3,返回false

进阶：
如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)

思路：进阶问题的关键是将链表的右半部分反转，然后再进行比较，注意把
改变的状态变回来
"""


from linkedlist.toolcls import Node


class HuiWen:
    @classmethod
    def is_huiwen(cls, head):
        if head is None or head.next is None:
            return True
        cur = head
        right = head.next
        stack = list()

        while cur.next is not None and cur.next.next is not None:
            right = right.next
            cur = cur.next.next

        while right is not None:
            stack.append(right.value)
            right = right.next

        cur = head
        while len(stack) != 0:
            if stack.pop() != cur.value:
                return False
            cur = cur.next

        return True

    @classmethod
    def is_huibwen_by_reverse_right(cls, head):
        if head is None or head.next is None:
            return True

        node = head
        right = node.next
        right_pre = head

        while node.next is not None and node.next.next is not None:
            right_pre = right
            right = right.next
            node = node.next.next

        node = head
        reversed_right = cls.reverse(right)
        temp = reversed_right

        while reversed_right is not None:
            if reversed_right.value != node.value:
                return False
            reversed_right = reversed_right.next
            node = node.next

        right = cls.reverse(temp)
        right_pre.next = right

        return True

    @classmethod
    def reverse(cls, head):
        while head is None or head.next is None:
            return None

        pre = None

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
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(1)
    print(HuiWen.is_huibwen_by_reverse_right(node))
    print(HuiWen.is_huiwen(node))

    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(3)
    node.next.next.next.next = Node(2)
    node.next.next.next.next.next = Node(1)
    print(HuiWen.is_huibwen_by_reverse_right(node))
    print(HuiWen.is_huiwen(node))