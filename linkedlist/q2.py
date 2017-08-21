"""
问题描述：分别实现两个函数，一个可以删除单链表中倒数第K个节点，另一个
可以删除双链表中倒数第K个节点

要求：如果链表长度为N，时间复杂度达到O(N),额外空间复杂度达到O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class RemoveTool:
    @classmethod
    def remove_last_k_node(cls, head, k):
        if head is None or k < 1:
            return head

        node = head
        while node is not None:
            node = node.next
            k -= 1

        if k > 0:
            return head
        elif k == 0:
            return head.next
        else:
            pre = None
            node = head
            while k < 0:
                k += 1
                pre = node
                node = node.next
            pre.next = node.next
        return head

    @classmethod
    def remove_last_k_node_from_double(cls, head, k):
        if head is None or k < 1:
            return head

        node = head
        while node is not None:
            node = node.next
            k -= 1

        if k > 0:
            return head
        elif k == 0:
            head.next.pre = None
            return head.next
        else:
            node = head
            while k < 0:
                k += 1
                node = node.next
            node.next.pre = node.pre
            node.pre.next = node.next

        return head

    @classmethod
    def print_list(cls, head):
        while head is not None:
            print(head.value, end=' ')
            head = head.next
        print()

if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(4)
    node1.next.next.next.next = Node(5)
    node1.next.next.next.next.next = Node(6)
    cnode = RemoveTool.remove_last_k_node(node1, 5)
    RemoveTool.print_list(cnode)

    node2 = DoubleNode(1)
    node2.next = DoubleNode(2)
    node2.next.pre = node2
    node2.next.next = DoubleNode(3)
    node2.next.next.pre = node2.next
    node2.next.next.next = DoubleNode(4)
    node2.next.next.next.pre = node2.next.next
    node2.next.next.next.next = DoubleNode(5)
    node2.next.next.next.next.pre = node2.next.next.next
    node2.next.next.next.next.next = DoubleNode(6)
    node2.next.next.next.next.next.pre = node2.next.next.next
    dcnode = RemoveTool.remove_last_k_node_from_double(node2, 5)
    RemoveTool.print_list(dcnode)