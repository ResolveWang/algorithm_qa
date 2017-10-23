"""
问题描述：平衡二叉树的性质是：要么是一棵空树，要么任何一个节点的左右子树的高度差
的绝对值bu超过1。现在给定一棵二叉树的头结点head，请判断它是否是一棵平衡二叉树。
"""

from binarytree.toolcls import Node


class BlanceTreeTool:
    res = True

    @classmethod
    def is_blanced_tree(cls, head, height):
        res = [1]
        cls.get_height(head, 0, res)
        return True if res[0] == 1 else False

    @classmethod
    def get_height(cls, head, height, res):
        if head is None:
            return height

        left = cls.get_height(head.left, height + 1, res)

        right = cls.get_height(head.right, height + 1, res)

        val = (left - right) if left > right else (right - left)

        if val > 1:
            res[0] = 0

        return max(left, right)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    print(BlanceTreeTool.is_blanced_tree(head, 0))