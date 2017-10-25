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
    def is_complete_tree(cls, head):
        if head is None:
            return True
        my_queue = list()
        my_queue.append(head)
        to_leaf = 0
        while len(my_queue) > 0:
            node = my_queue.pop(0)
            if node.left is not None and node.right is not None:
                if to_leaf == 1:
                    return False
                my_queue.append(node.left)
                my_queue.append(node.right)
            if node.left is None and node.right is not None:
                return False
            if node.left is not None and node.right is None:
                if to_leaf == 1:
                    return False
                to_leaf = 1
                my_queue.append(node.left)
            if not node.left and not node.right:
                if not to_leaf:
                    to_leaf = 1
        return True


if __name__ == '__main__':
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)

    print(JudgeTool.is_bst_tree(head))
    print(JudgeTool.is_complete_tree(head))