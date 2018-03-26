"""
问题描述:在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or pHead.next is None:
            return pHead
        head = pHead
        node = pHead
        pre_diff = node
        # head is not changed
        head_changed = False

        while node is not None:
            delete_node = False
            while node.next is not None and node.val != node.next.val:
                pre_diff = node
                node = node.next

            # while cur.val == next.val, delete them
            while node.next is not None and node.val == node.next.val:
                if head.val == node.val:
                    head_changed = True
                delete_node = True
                node = node.next

            # check whether the head is deleted
            if head_changed:
                node = node.next
                head = node
                pre_diff = head
                head_changed = False
                continue

            # head not deleted, the middle nodes are deleted
            if delete_node:
                pre_node = node
                pre_diff.next = node.next
                pre_node.next = None

            node = node.next

        return head

    def print_linked_list(self, phead):
        while phead:
            print(phead.val, end=' ')
            phead = phead.next


if __name__ == '__main__':
    phead = ListNode(1)
    phead.next = ListNode(1)
    phead.next.next = ListNode(2)
    phead.next.next.next = ListNode(3)
    phead.next.next.next.next = ListNode(3)

    s = Solution()
    cur_head = s.deleteDuplication(phead)
    s.print_linked_list(cur_head)
