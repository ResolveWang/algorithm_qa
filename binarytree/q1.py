"""
问题描述：分别用递归和非递归方式实现二叉树的先序、中序、和后续遍历

思路：使用非递归的方式需要使用辅助栈代替函数栈
"""


class RecursiveVisit:
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        print(head.value)
        cls.visit_in_first_order(head.left)
        cls.visit_in_first_order(head.right)

    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        cls.visit_in_first_order(head.left)
        print(head.value)
        cls.visit_in_first_order(head.right)

    @classmethod
    def visit_in_last_order(cls, head):
        if head is None:
            return
        cls.visit_in_first_order(head.left)
        cls.visit_in_first_order(head.right)
        print(head.value)


class LoopVisit:
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        stack = list()
        stack.append(head)
        while len(stack) > 0:
            node = stack.pop()
            print(node.value)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        stack = list()
        if head.right is not None:
            stack.append(head.right)
        stack.append(head.value)
        if head.left is not None:
            stack.append(head.left)

    @classmethod
    def visit_in_last_order(cls, head):
        pass