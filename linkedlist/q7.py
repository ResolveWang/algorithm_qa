"""
问题描述：给定一个链表的头结点，请判断该链表是否为回文结构，例如：
1->2->1,返回true
1->2->2->1,返回true
15->6->15,返回true
1->2->3,返回false

进阶：
如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)
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


if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(1)

    print(HuiWen.is_huiwen(node))