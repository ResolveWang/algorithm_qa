"""
问题描述：一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是搜索二叉树，
请找到这两个节点并返回。已知二叉树所有节点的值都不一样，给定二叉树的头结点head,返回一个长度为2的
二叉树节点类型的数组errs。errs[0]表示一个错误节点，errs[1]表示一个错误节点。
进阶：如果在原问题中得到了这两个错误节点，我们当然可以通过交换两个节点值的方式让整棵二叉树重新成为
搜索二叉树，但现在要求不能这么做，而是在结构上完全交换两个节点的位置，请实现调整的函数。
"""

from binarytree.toolcls import Node


# todo 完成进阶题目
class BSTChecker:
    def __init__(self):
        self.nodes = list()
        self.errors = list()

    def get_wrong_nodes(self):
        for index, node in enumerate(self.nodes[:-1]):
            if node.value > self.nodes[index+1].value:
                self.errors.append((node, self.nodes[index+1]))
        if len(self.errors) == 1:
            return list(self.errors[0])

        if len(self.errors) == 2:
            return [self.errors[0][0], self.errors[1][1]]

    def get_all_nodes(self, head):
        if head is None:
            return None
        if head.left is not None:
            self.get_all_nodes(head.left)
        self.nodes.append(head)
        if head.right is not None:
            self.get_all_nodes(head.right)


if __name__ == '__main__':
    head14 = Node(5)
    head14.left = Node(3)
    head14.right = Node(7)
    head14.left.left = Node(2)
    head14.left.right = Node(8)
    head14.right.left = Node(6)
    head14.right.right = Node(4)
    head14.left.left.left = Node(1)

    bst = BSTChecker()
    bst.get_all_nodes(head14)
    err_nodes = bst.get_wrong_nodes()
    for err_node in err_nodes:
        print(err_node.value)


