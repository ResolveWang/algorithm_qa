"""
问题描述：一个环形单链表从头结点head开始不降序，同时由最后的节点指回头结点。给定这样一个
环形单链表的头结点head和一个整数num,请生成节点值为num的新节点，并插入到这个环形链表中，
保证调整后的链表依然有序。
"""

from linkedlist.toolcls import Node


class InsertTool:
    @classmethod
    def insert_node_by_order(cls, head, num):
        node = Node(num)
        if head is None:
            node.next = node
            return node

        pre = None
        cur = head
        while True:
            if head.next == head:
                tail = head
                break
            if pre is not None and pre.value > cur.value:
                tail = pre
                break
            pre = cur
            cur = cur.next

        pre = None
        cur = head
        while True:
            if pre is not None and pre.value > cur.value:
                break
            if cur.value > node.value:
                if pre is not None:
                    pre.next = node
                    node.next = cur
                    return head
                else:
                    node.next = cur
                    tail.next = node
                    return node
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = head
        return head

    @classmethod
    def print_list(cls, head):
        if head is None:
            print('None')
        if head is not None and head.next == head:
            print(head.value)
            return
        pre = None
        cur = head
        while True:
            if pre is not None and pre.value > cur.value:
                return
            print(cur.value, end=' ')
            pre = cur
            cur = cur.next


if __name__ == '__main__':
    head = None
    head = InsertTool.insert_node_by_order(head, 2)
    head = InsertTool.insert_node_by_order(head, 1)
    head = InsertTool.insert_node_by_order(head, 4)
    head = InsertTool.insert_node_by_order(head, 3)
    head = InsertTool.insert_node_by_order(head, 5)
    head = InsertTool.insert_node_by_order(head, 0)
    InsertTool.print_list(head)
