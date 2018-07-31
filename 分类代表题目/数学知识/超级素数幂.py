"""
问题描述: 如果一个数字能表示为p^q(^表示幂运算)且p为一个素数,q为大于1的正整数就称这个数叫做超级素数幂。
现在给出一个正整数n,如果n是一个超级素数幂需要找出对应的p,q。

输入描述:
输入一个正整数n(2 ≤ n ≤ 10^18)
输出描述:
如果n是一个超级素数幂则输出p,q,以空格分隔,行末无空格。 如果n不是超级素数幂，则输出No
示例1
输入
27

输出
3 3
"""

import sys
import math


class Solution:
    def get_super_num(self, num):
        q_max = math.sqrt(num)
        q = 2
        while q <= q_max:
            p = num ** (1.0 / q)
            if p == int(p) and self.is_prime(int(p)):
                print(str(int(p)) + ' ' + str(q))
                return
            q += 1
        print('No')

    def is_prime(self, num):
        if n < 2:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = Solution()
    s.get_super_num(n)