"""
问题描述：给定一个二叉树的头结点head，已知其中没有重复值的节点，实现两个函数分别判断这棵二叉树是否是
搜索二叉树和完全二叉树。
"""


from binarytree.toolcls import Node


class JudgeTool:
    @classmethod
    def is_bst_tree(cls, head):
        if head is None:
            return True
        res = [True]
        cls.is_bst_tree_detail(head, None, '', res)
        return res[0]

    @classmethod
    def is_bst_tree_detail(cls, head, pre, relation, res):
        if head.left:
            cls.is_bst_tree_detail(head.left, head, 'left', res)
        if pre is not None:
            if relation == 'left':
                if pre.value < head.value:
                    res[0] = False
            else:
                if pre.value > head.value:
                    return False
        if head.right:
            cls.is_bst_tree_detail(head.right, head, 'right', res)

    @classmethod
    def is_full_tree(cls, head):
        pass


if __name__ == '__main__':
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)

    print(JudgeTool.is_bst_tree(head))