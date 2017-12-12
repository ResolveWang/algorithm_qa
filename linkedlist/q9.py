"""
问题描述：一种特殊的链表节点类描述如下：
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None

Node类中的value是节点值，next指针和正常单链表中next指针的意义一样，都指向下一个节点，rand
指针是Node类中新增的指针，这个指针可能指向链表中任意一个节点，也可能指向None.

给定一个由Node节点类型组成的无环单链表的头结点head，请实现一个函数完成这个链表中所有结构的复
制，并返回复制的新链表的头结点。例如：链表 1->2->3->None,假设1的rand指针指向3，2的rand指
针指向None,3的rand指针指向1。复制后的链表应该也是这种结构，比如,1'->2'->3'->None,1'的
rand指针指向3',2'的rand指针指向None，3'的rand指针指向1',最后返回1'

进阶：不使用额外的数据结构，只用有限几个变量，且在时间复杂度为O(N)内完成原问题要实现的函数。

思路：
1）如果不考虑空间复杂度，可使用hashmap求解
2）由于复制的链表和原链表具有操作一致性，所以可以直接在原链表中每个元素后插入一个和前一个一样的
元素，两两元素的取node.rand操作必定是一致的
"""


from linkedlist.toolcls import PrintMixin


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None


class CopyList(PrintMixin):
    @classmethod
    def copy_list_use_map(cls, head):
        if head is None:
            return head

        temp_map = {}
        node = head

        while node is not None:
            temp_map.setdefault(node, Node(node.value))
            node = node.next

        node = head

        while node is not None:
            new_node = temp_map.get(node)
            new_node.next = temp_map.get(node.next)
            new_node.rand = temp_map.get(node.rand)
            node = node.next

        return temp_map.get(head)

    @classmethod
    def copy_list(cls, head):
        if head is None:
            return head
        node = head
        while node is not None:
            next_node = node.next
            new_next = Node(node.value)
            node.next = new_next
            new_next.next = next_node
            node = next_node

        node = head
        new_node = head.next
        while node is not None:
            if node.rand is not None:
                new_node.rand = node.rand.next
            else:
                new_node.rand = None

            node = node.next.next
            if node is not None:
                new_node = node.next

        origin = head
        res = head.next
        while origin is not None:
            next = origin.next.next
            new_node = origin.next
            if next is not None:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            origin.next = next
            origin = next

        return res


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.rand = head.next.next.next.next.next
    head.next.rand = head.next.next.next.next.next
    head.next.next.rand = head.next.next.next.next
    head.next.next.next.rand = head.next.next
    head.next.next.next.next.rand = None
    head.next.next.next.next.next.rand = head.next.next.next

    res1 = CopyList.copy_list_use_map(head)
    CopyList.print_list_rand(res1)

    res2 = CopyList.copy_list(head)
    CopyList.print_list_rand(res2)