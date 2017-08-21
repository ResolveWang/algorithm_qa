"""
问题描述：给定链表的头结点head,实现删除链表的中间节点的函数，例如：
不删除任何节点；
1->2,删除节点1；
1->2->3,删除节点2；
1->2->3->4，删除节点2；
1->2->3->4->5，删除节点3；
进阶：
给定链表头节点head、整数a和b，实现删除位于a/b节点处的函数，例如：
链表1->2->3->4->5,假设a/b的值为r。
如果r等于0，不删除任何节点；
如果r在区间(0, 1/5]之间，删除节点1；
如果r在区间(1/5, 2/5]之间，删除节点2；
如果r在区间(2/5, 3/5]之间，删除节点3；
如果r在区间(3/5, 4/5]之间，删除节点4；
如果r在区间(4/5, 1]之间，删除节点5；
如果r大于1，不删除任何节点。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class RemoveNode:
    @classmethod
    def print_linkedlist(cls, head):
        while head is not None:
            print(head.value, end=' ')
            head = head.next
        print()

    @classmethod
    def remove_mid_node(cls, head):
        if head is None or head.next is None:
            return head

        if head.next.next is None:
            return head.next

        pre = head
        cur = head.next.next

        while cur.next is not None and cur.next.next is not None:
            cur = cur.next.next
            pre = pre.next

        pre.next = pre.next.next

        return head

if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(4)
    node.next.next.next.next = Node(5)
    node.next.next.next.next.next = Node(6)

    node = RemoveNode.remove_mid_node(node)
    RemoveNode.print_linkedlist(node)