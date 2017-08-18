"""
问题描述：给定一个整型矩阵map，其中的值只有0和1两种，求其中全是1的所有矩形区域中，
最大的矩形区域为1的数量，例如：
1 1 1 0
其中，最大的矩形区域有3个1，所以返回3
再如：
1 0 1 1
1 1 1 1
1 1 1 0
其中，最大的矩形区域有6个1，所以返回6

思路：
1）将矩阵按行分割，并将上一行的结果迭代到下一行
2）可将（1）的结果看做一个直方图，然后使用单调栈比较以每个块为基础的最大面积
"""


class MaxMaxtrix:
    @classmethod
    def get_maxtrix(cls, arr):
        pre = None
        max_value = 0
        for each in arr:
            if pre is not None:
                for index, value in enumerate(each):
                    if value != 0:
                        each[index] = each[index] + pre[index]
            pre = each
            cur_value = cls.get_maxarea_in_arr(each)
            if cur_value > max_value:
                max_value = cur_value
        return max_value

    @classmethod
    def get_maxarea_in_arr(cls, arr):
        stack = list()
        values = 0
        for index, value in enumerate(arr):
            while len(stack) != 0 and value <= arr[stack[-1]]:
                j = stack.pop()
                if len(stack) == 0:
                    k = -1
                else:
                    k = stack[-1]
                area = (index - k - 1) * arr[j]
                if values < area:
                    values = area

            stack.append(index)

        max_len = len(arr)
        while len(stack) != 0:
            j = stack.pop()
            if len(stack) == 0:
                k = -1
            else:
                k = stack[-1]
            area = (max_len - k - 1) * arr[j]
            if values < area:
                values = area
        return values

if __name__ == '__main__':
    print(MaxMaxtrix.get_maxtrix([[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]))