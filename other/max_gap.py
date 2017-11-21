"""
问题描述：给定一个无序数组，求如果有序之后相邻两个元素最大的差值。

要求：时间复杂度为O(N)

比如 3,4,0,9,10,排序之后是0,3,4,9,10
相邻两数最大差值是5

思想：由于要求时间复杂度为O(N)，所以无法使用基于比较的排序算法，可以
借用桶排序的思想。
"""


class MaxGapFounder:
    @classmethod
    def get_max_gap(cls, arr):
        if not arr or len(arr) < 2:
            return 0

        max_value = max(arr)
        min_value = min(arr)
        length = len(arr)

        if max_value == min_value:
            return 0

        has_num = [False for _ in range(length+1)]
        max_values = [0 for _ in range(length+1)]
        min_values = [0 for _ in range(length+1)]

        for index, value in enumerate(arr):
            pos = cls.bucket(value, length, max_value, min_value)
            max_values[pos] = max([max_values[pos], value]) if has_num[pos] else value
            min_values[pos] = min([min_values[pos], value]) if has_num[pos] else value
            has_num[pos] = True

        max_gap = 0
        i = 1
        last_max = max_values[0]
        while i <= length:
            if has_num[i]:
                max_gap = max(min_values[i] - last_max, max_gap)
                last_max = max_values[i]
            i += 1

        return max_gap

    @classmethod
    def bucket(cls, num, length, max_value, min_value):
        return int((num - min_value)/(max_value - min_value) * length)


if __name__ == '__main__':
    my_arr = [3, 4, 0, 9, 10]
    print(MaxGapFounder.get_max_gap(my_arr))