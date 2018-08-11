"""
问题描述: 有n堆苹果，每堆a[i]个，打印出在m次查询中，每次查询
对应的苹果位于哪个堆中。比如

输入:
3
2 5 10
2
12 5

输出:
3
2

"""


import sys


class Solution:
    def get_apple_pos(self, apples, queries):
        heaps = self.pre_process(apples)
        for query in queries:
            self.find_pos_by_num(heaps, query)

    def find_pos_by_num(self, heaps, query):
        start = 0
        end = len(heaps) - 1
        while True:
            index = (start + end) >> 1
            if heaps[index][0] <= query <= heaps[index][1]:
                print(index + 1)
                return
            elif query > heaps[index][1]:
                start = index + 1
            else:
                end = index - 1

    def pre_process(self, apples):
        heaps = list()
        left = 0
        right = 0
        for i in apples:
            right += i
            heaps.append((left, right))
            left = right + 1
        return heaps


if __name__ == '__main__':
    n = sys.stdin.readline()
    ap_arr = list(map(int, sys.stdin.readline().split()))
    m = sys.stdin.readline()
    q_arr = list(map(int, sys.stdin.readline().split()))

    solution = Solution()
    solution.get_apple_pos(ap_arr, q_arr)
