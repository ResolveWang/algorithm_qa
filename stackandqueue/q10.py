"""
问题描述：给定数组arr和整数num，共返回有多少个子数组满足如下情况：
max(arr[i...j])-max(arr[i...j]) <= num
max(arr[i...j])表示子数组arr[i..j]中的最大值，min(arr[i..j])
表示子数组中的最小值。

要求：如果数组长度为N，实现时间复杂度为O(N)的解法。

思路：双向队列模拟动态窗口（单调队列），qmax单调递减，而qmin单调递增。
从i=0,j=0开始，j往后扩，直到不能扩为止，arr[i,j-1]肯定是满足需求的，
这时候再让i+1，再让j继续往后扩
"""


class MaxNumOfSubArr:
    @classmethod
    def get_num_of_sub_arr(cls, arr, num):
        if len(arr) == 0:
            return 0

        qmin = list()
        qmax = list()
        j = 0
        res = 0

        for index, value in enumerate(arr):
            while j < len(arr):
                while len(qmin) != 0 and arr[qmin[-1]] >= arr[j]:
                    qmin.pop()
                qmin.append(j)

                while len(qmax) != 0 and arr[qmax[-1]] <= arr[j]:
                    qmax.pop()
                qmax.append(j)

                if arr[qmax[0]] - arr[qmin[0]] > num:
                    break
                j += 1

            if len(qmin) > 0 and qmin[0] == index:
                qmin.pop(0)
            if len(qmax) > 0 and qmax[0] == index:
                qmax.pop(0)
            res += (j - index)

        return res


if __name__ == '__main__':
    cur_num = 5
    cur_arr = [2, 4, 1, 9, 5]
    print(MaxNumOfSubArr.get_num_of_sub_arr(cur_arr, cur_num))