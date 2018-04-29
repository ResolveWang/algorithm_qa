"""
问题: 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例:
n = 3, k = 3 => "213"
"""


import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n < 1:
            return ''

        r = 1
        tmp = n
        while tmp > 0:
            r *= tmp
            tmp -= 1
        if r < k or k <= 0:
            return ''

        datas = list(range(1, n + 1))
        step = n
        res = list()
        while len(datas) > 1:
            r = r / step
            cur_pos = math.ceil(k / r) - 1
            res.append(datas[cur_pos])
            datas = datas[:cur_pos] + datas[cur_pos + 1:]
            k = k % r
            if k == 0:
                k = r
            step -= 1

        if len(datas) == 1:
            res.append(datas[0])

        return ''.join(map(str, res))