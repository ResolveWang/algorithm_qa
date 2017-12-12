"""
问题描述：给定一个无序单链表的头结点head，删除其中值重复出现的节点。
例如：1->2->3->3->4->4->2->1->1->None，删除值重复的节点之后为
1->2->3->4_None.
要求：分别按以下要求实现两种方法
1)如果链表长度为N，时间复杂度为O(N)
2)额外空间复杂度为O(1)

思路：
1）使用hashmap辅助
2）遍历即可
"""

from linkedlist.toolcls import Node, PrintMixin


class DuplicatedNodeRemove(PrintMixin):
    @classmethod
    def remove_duplicate_node(cls, head):
        if head is None or head.next is None:
            return head
        node_set = set()
        pre = None
        cur = head
        while cur is not None:
            if cur.value not in node_set:
                node_set.add(cur.value)
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next

        return head

    @classmethod
    def remove_duplicate_node2(cls, head):
        if head is None or head.next is None:
            return head
        cur = head
        pre = None
        flag = 0
        while cur is not None:
            fake_head = head
            while fake_head != cur:
                next = cur.next
                if fake_head.value == cur.value:
                    # del current
                    pre.next = next
                    flag = 1
                    break
                fake_head = fake_head.next
            if flag != 1:
                pre = cur
            cur = cur.next
            flag = 0
        return head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next.next.next = Node(1)
    DuplicatedNodeRemove.print_list(DuplicatedNodeRemove.remove_duplicate_node(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next.next.next = Node(1)
    DuplicatedNodeRemove.print_list(DuplicatedNodeRemove.remove_duplicate_node2(head))
