"""
问题描述: 给定两个32位整数a和b，可正、可负、可０。不能使用算术运算符，实现a和b的加减乘除运算。

要求：
如果给定的a和b执行加减乘除的某些结果本来就会导致数据的溢出，那么你实现的结果不必对那些结果负责。
"""


class BitOperation:
    @classmethod
    def add(cls, x, y):
        value = x
        while y != 0 and pow(2, 31) >= y:
            # import time
            # time.sleep(0.5)
            # print(y)
            value = (x ^ y)
            y = ((x & y) << 1)
            x = value

        return value

    @classmethod
    def get_opposite(cls, args):
        return cls.add(~args, 1)

    @classmethod
    def minus(cls, x, y):
        new_y = cls.get_opposite(y)
        return cls.add(x, new_y)

    @classmethod
    def multi(cls, x, y):
        res = 0
        while y != 0:
            tmp = (y & 1)
            if tmp != 0:
                res = cls.add(x, res)
            y = (y >> 1)
            x = (x << 1)

        return res


if __name__ == '__main__':
    a = 5
    b = 4
    print(BitOperation.add(a, b))
    print(BitOperation.minus(a, -b))
    print(BitOperation.multi(a, b))