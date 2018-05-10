"""
问题描述: 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。


示例:
4->2->1->3 => 1->2->3->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = head
        slow = head
        fast = head
        # 通过快慢指针获取前半段和后半段
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 注意在链表操作的时候，一定要把尾指针置为None
        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        if not h1:
            return h2

        if not h2:
            return h1

        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2