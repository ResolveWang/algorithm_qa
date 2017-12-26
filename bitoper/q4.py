"""
问题描述：给定一个３２位整数n,可为０、正或者负，返回该整数二进制表达式中１的个数。
"""


class BitCounter:
    @classmethod
    def count(cls, n):
        if n < 0:
            return 32
        res = 0
        while n != 0:
            res += (n & 1)
            n = n >> 1
        return res

    @classmethod
    def count2(cls, n):
        res = 0
        while n != 0:
            n = (n & (n-1))
            res += 1
        return res

    @classmethod
    def count3(cls, n):
        res = 0
        while n != 0:
            n -= (n & (~n+1))
            res += 1
        return res


if __name__ == '__main__':
    num = 65535
    print(BitCounter.count(num))
    print(BitCounter.count2(num))
    print(BitCounter.count3(num))