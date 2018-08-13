"""
问题描述: 在一个长为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少
有一个数字是重复的，找出任意一个重复的数字即可，但是不能改变输入的数组，要求
空间复杂度为O(1)
"""


class Solution:
    def get_duplicate_num(self, arr):
        start = 1
        end = len(arr) - 1
        while start <= end:
            mid = ((end - start) >> 1) + start
            num = self.count(arr, start, mid)
            if start == end:
                if num > 1:
                    return start

            if num > (mid-start+1):
                end = mid
            else:
                start = mid + 1

        return None

    def count(self, arr, start, end):
        count = 0
        for i in arr:
            if start <= i <= end:
                count += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    array = [2, 3, 5, 4, 3, 2, 6, 7]
    r = solution.get_duplicate_num(array)
    print(r)

    array = [1, 2, 3, 4]
    r = solution.get_duplicate_num(array)
    print(r)