"""
问题描述：给定一棵二叉树的头结点head，完成二叉树的先序、中序和后序遍历。如果节点数为N，
要求时间复杂度为O(N)，额外空间复杂度为O(1)

思路:将子树最右边节点的空指针指向子树的头结点，即Morris遍历
"""


from binarytree.toolcls import Node


class TreeVisit:
    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        node1 = head
        while node1 is not None:
            node2 = node1.left
            if node2 is not None:
                while node2.right is not None and node2.right != node1:
                    node2 = node2.right
                if node2.right is None:
                    node2.right = node1
                    node1 = node1.left
                    continue
                else:
                    node2.right = None
            print(node1.value, end=' ')
            node1 = node1.right

    @classmethod
    def visit_in_pre_order(cls, head):
        if head is None:
            return
        node1 = head
        while node1 is not None:
            node2 = node1.left
            if node2 is not None:
                while node2.right is not None and node2.right != node1:
                    node2 = node2.right
                if node2.right is None:
                    print(node1.value, end=' ')
                    node2.right = node1
                    node1 = node1.left
                    continue
                else:
                    node2.right = None
            else:
                print(node1.value, end=' ')
            node1 = node1.right

    @classmethod
    def visit_in_last_order(cls, head):
        if head is None:
            return
        node1 = head
        while node1 is not None:
            node2 = node1.left
            if node2 is not None:
                while node2.right is not None and node2.right != node1:
                    node2 = node2.right
                if node2.right is None:
                    node2.right = node1
                    node1 = node1.left
                    continue
                else:
                    node2.right = None
                    cls.print_edge(node1.left)
            node1 = node1.right
        cls.print_edge(head)

    @classmethod
    def print_edge(cls, head):
        tail = cls.reverse_right_tree(head)
        cur = tail
        while cur is not None:
            print(cur.value, end=' ')
            cur = cur.right
        cls.reverse_right_tree(tail)

    @classmethod
    def reverse_right_tree(cls, head):
        pre = None
        cur = head

        while cur is not None:
            right = cur.right
            cur.right = pre
            pre = cur
            cur = right
        return pre


if __name__ == '__main__':
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(7)

    TreeVisit.visit_in_mid_order(head)
    print()
    TreeVisit.visit_in_pre_order(head)
    print()
    TreeVisit.visit_in_last_order(head)