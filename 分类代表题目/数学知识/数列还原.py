"""
问题描述: 牛牛的作业薄上有一个长度为 n 的排列 A，这个排列包含了从1到n的n个数，但是因为一些原因，
其中有一些位置（不超过 10 个）看不清了，但是牛牛记得这个数列顺序对的数量是 k，顺序对是指满足 i < j
且 A[i] < A[j] 的对数，请帮助牛牛计算出，符合这个要求的合法排列的数目。

输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含两个整数 n 和 k（1 <= n <= 100, 0 <= k <= 1000000000），
接下来的 1 行，包含 n 个数字表示排列 A，其中等于0的项表示看不清的位置（不超过 10 个）。


输出描述:
输出一行表示合法的排列数目。
示例1
输入
5 5
4 0 0 2 0
输出
2
"""
import sys
import itertools


class Solution:
    def get_rs(self, arr, k):
        rs = 0
        num1 = self.counter(arr)
        k -= num1
        lacked = set(range(1, len(arr) + 1)) - set(filter(lambda x: x != 0, arr))
        lacked_pos = list()
        origin_pos = list()
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                lacked_pos.append(index)
            else:
                origin_pos.append(index)
            index += 1

        datas = itertools.permutations(lacked)
        for data in datas:
            num2 = self.counter(data)
            num3 = self.count_two_arr(arr, data, origin_pos, lacked_pos)
            if num2 + num3 == k:
                rs += 1
        print(rs)

    def counter(self, arr):
        count = 0
        i = 0
        while i < len(arr) - 1:
            j = i + 1
            while j < len(arr):
                if arr[i] != 0 and arr[i] < arr[j]:
                    count += 1
                j += 1
            i += 1
        return count

    def count_two_arr(self, arr1, arr2, origin, lacked):
        count = 0
        for index, i in enumerate(lacked):
            for j in origin:
                if (j < i and arr1[j] < arr2[index]) or (i < j and arr2[index] < arr1[j]):
                    count += 1

        return count


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    args = list(map(int, sys.stdin.readline().split()))
    s = Solution()
    s.get_rs(args, b)