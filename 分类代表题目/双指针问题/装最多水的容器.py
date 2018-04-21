"""
问题: 给定 n 个非负整数 a1, a2, ..., an, 每个数代表了坐标中的一个点 (i, ai)。画 n 条垂直线，
使得 i 垂直线的两个端点分别为(i, ai)和(i, 0)。找到两条线，使得其与 x 轴共同构成一个容器，以容纳
最多水。

示例: [1, 3, 2, 4]  选择[3, 2, 4]，容量最大为 3*2 = 6

方法: 双指针两边逼近法
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length <= 1:
            return 0

        right_index = len(height) - 1
        left_index = 0
        max_area = 0
        while left_index < right_index:
            max_area = max([max_area, (right_index - left_index) *
                            min([height[right_index], height[left_index]])])
            if height[right_index] < height[left_index]:
                right_index -= 1
            else:
                left_index += 1

        return max_area