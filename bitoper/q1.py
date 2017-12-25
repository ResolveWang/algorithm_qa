"""
问题描述：如何不借助任何额外变量交换两个整数的值？
"""


class ValueSwap:
    @classmethod
    def swap(cls, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b

        return a, b


if __name__ == '__main__':
    a, b = 2, 3
    print(ValueSwap.swap(a, b))