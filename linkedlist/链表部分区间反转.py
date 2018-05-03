"""
问题: 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。说明: 1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

注意点:
与单链表整体反转不同，这里需要注意头结点是否改变
"""


class Solution:
    def reverseBetween(self, head, m, n):
        count = 1
        pre = None
        cur = head
        while count < m:
            pre = cur
            cur = cur.next
            count += 1

        pre2 = None
        rotated_node = None
        while count <= n and cur:
            next_node = cur.next
            if not rotated_node:
                rotated_node = cur
            cur.next = pre2
            pre2 = cur
            cur = next_node
            count += 1

        if pre:
            pre.next = pre2

        if rotated_node:
            rotated_node.next = cur

        return head if pre else pre2