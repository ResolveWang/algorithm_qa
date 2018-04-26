"""
问题描述: 给定一个正整数n,求它的阶乘结果中末尾的0的个数
例子: 11! = 39916800 => 2

思路:
这道题是一个数学问题，0的个数取决于10的因数个数，而对10进行因数
分解，最终由5这个质数进行决定
num = n/5 + n/(5*5) + n/(5*5*5) + ... + n/(5*5*...*5)
"""


class Solution:
    def get_zeros(self, num):
        res = 0
        while num > 0:
            res += int(num/5)
            num = int(num/5)
        return res