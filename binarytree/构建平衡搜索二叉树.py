"""
问题: 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。本题中，一个高度平衡二叉树
是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

思路:
在构建二叉树系列问题中，我们可以使用前序遍历，只要收集好构建二叉树节点关系的信息就可以了,一般左右节点都
直接调用递归获取即可
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        arr = list()
        while head:
            arr.append(head.val)
            head = head.next
        return self.process(arr, 0, len(arr) - 1)

    def process(self, nums, start, end):
        if start > end:
            return

        cur_index = (start + end) >> 1
        cur = TreeNode(nums[cur_index])

        cur.left = self.process(nums, start, cur_index - 1)
        cur.right = self.process(nums, cur_index + 1, end)

        return cur