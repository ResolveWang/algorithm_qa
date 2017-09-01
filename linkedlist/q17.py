"""
问题描述：链表节点值类型为int型，给定一个链表中的节点，但不给定整个链表
的表头，如何在链表中删除node?请实现这个函数，并分析会出现哪些问题？
要求：时间复杂度为O(1)

思路：将待删除节点的下一个节点的值赋值给待删除节点，直接删除下一个节点

分析：这样做的坏处是：1）无法删除最后一个节点；2）这种删除方式本质上根本不是删除
node节点，而是把node节点的值改变，然后删除node的下一个节点，在实际的工程中可能
会带来很大的问题，比如工程上一个节点代表一个提供服务的服务器，外界对每个节点都有
很多依赖，那么在上述方法中，实际上影响的是节点3，它会无法对外提供服务，再如，节点
可能代表很复杂的结构，节点值的复制会相当复杂，可能改变节点值的这个操作都是被禁止的。
"""


from linkedlist.toolcls import Node, PrintMixin


class RemoveNode(PrintMixin):
    @classmethod
    def remove_node(cls, node):
        if node is None:
            return
        if node.next is None:
            raise RuntimeError("it can't be removed")
        node.value = node.next.value
        new_next = node.next.next
        del node.next
        node.next = new_next

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    node = head
    RemoveNode.print_list(head)
    RemoveNode.remove_node(node)
    RemoveNode.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    node = head.next
    RemoveNode.print_list(head)
    RemoveNode.remove_node(node)
    RemoveNode.print_list(head)