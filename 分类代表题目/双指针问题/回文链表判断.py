"""
问题: 请判断一个链表是否为回文链表

要求:
时间复杂度为O(N)，空间复杂度为O(1)
"""


import math


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length <= 1:
            return True

        count = 1
        cur = head
        half = math.ceil(length / 2)
        while count < half:
            cur = cur.next
            count += 1
        half_head = cur
        cur = cur.next
        node = self.reverse(cur)
        half_head.next = node

        fast = head
        slow = head
        count = 1
        while count <= half:
            fast = fast.next
            count += 1
        while fast:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next

        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre



