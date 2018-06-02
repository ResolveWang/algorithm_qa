"""
问题: 求一颗完全二叉树的所有节点数量

思路:
计算左子树和右子树高度是否相等
1.相等则说明左子树一定是满二叉树
2.不相等说明右子树一定是满二叉树
"""


class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)