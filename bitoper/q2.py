"""
问题描述：给定两个32位整数a和b，返回a和b中较大的

要求:
不能用任何比较判断
"""


class BiggerGetter:
    @classmethod
    def flip(cls, n):
        return n ^ 1

    @classmethod
    def sign(cls, n):
        return cls.flip((n >> 31) & 1)

    @classmethod
    def get_bigger_num(cls, a, b):
        c = a - b
        d = c >> 31 & 1
        e = d ^ 1
        f = e ^ 1
        return e*a + f*b

    @classmethod
    def get_bigger_the_right_way(cls, a, b):
        c = a - b
        sa = cls.sign(a)
        sb = cls.sign(b)
        sc = cls.sign(c)
        diffsasb = sa ^ sb
        samesasb = cls.flip(diffsasb)
        return_a = diffsasb * sa + samesasb * sc
        return_b = cls.flip(return_a)
        return return_a * a + return_b * b


if __name__ == '__main__':
    print(BiggerGetter.get_bigger_num(1, 2))
    print(BiggerGetter.get_bigger_the_right_way(1, 2))