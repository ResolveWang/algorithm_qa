"""
问题描述：分别用递归和非递归方式实现二叉树的先序、中序、和后续遍历

思路：使用非递归的方式需要使用辅助栈代替函数栈
"""


from binarytree.toolcls import Node


class RecursiveVisit:
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        print(head.value, end=' ')
        cls.visit_in_first_order(head.left)
        cls.visit_in_first_order(head.right)

    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        cls.visit_in_mid_order(head.left)
        print(head.value, end=' ')
        cls.visit_in_mid_order(head.right)

    @classmethod
    def visit_in_last_order(cls, head):
        if head is None:
            return
        cls.visit_in_last_order(head.left)
        cls.visit_in_last_order(head.right)
        print(head.value, end=' ')


class LoopVisit:
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        stack = list()
        stack.append(head)
        while len(stack) > 0:
            node = stack.pop()
            print(node.value, end=' ')

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        stack = list()
        cur = head
        while len(stack) > 0 or cur is not None:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                print(cur.value, end=' ')
                cur = cur.right

    @classmethod
    def visit_in_last_order(cls, head):
        if head is None:
            return
        stack1 = list()
        stack2 = list()

        cur = head
        stack1.append(cur)

        while len(stack1) > 0:
            cur = stack1.pop()
            if cur.left is not None:
                stack1.append(cur.left)
            if cur.right is not None:
                stack1.append(cur.right)

            stack2.append(cur.value)

        while len(stack2) > 0:
            print(stack2.pop(), end=' ')

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    RecursiveVisit.visit_in_first_order(head)
    print()
    LoopVisit.visit_in_first_order(head)
    print()
    print('===========================')

    RecursiveVisit.visit_in_mid_order(head)
    print()
    LoopVisit.visit_in_mid_order(head)
    print()
    print('===========================')
    RecursiveVisit.visit_in_last_order(head)
    print()
    LoopVisit.visit_in_last_order(head)
    print()