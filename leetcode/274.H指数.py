"""
问题描述:给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。
编写一个方法，计算出研究者的 h 指数。
h 指数的定义: “一位有 h 指数的学者，代表他（她）的 N 篇论文中至多有 h 篇论文，
分别被引用了至少 h 次，其余的 N - h 篇论文每篇被引用次数不多于 h 次。”

输入: citations = [3,0,6,1,5]
输出: 3
"""


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        if len(citations) == 1:
            if citations[0] > 0:
                return 1
            else:
                return 0

        citations.sort(reverse=True)
        index = 1
        while index <= len(citations):
            if index < len(citations):
                if citations[index] <= index <= citations[index - 1]:
                    return index
            elif index == len(citations):
                if citations[index - 1] >= index:
                    return index

            index += 1

        return 0