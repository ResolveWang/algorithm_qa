"""
问题描述:给定一个整型数组arr和一个大于１的整数k。已知arr中只有１个数出现了１次，
其它的数都出现了k次，请返回只出现了１次的数。

要求:
时间复杂度为O(N)，额外空间复杂度为O(1).

思路：
k个k进制的数，无进位相加。比如２个相同的二进制的数，无进位相加，结果一定为0
"""


class KGetter:
    @classmethod
    def num2ksys(cls, num, k):
        res = [0 for _ in range(32)]
        i = 0
        while num != 0:
            res[i] = num % k
            num = int(num / k)
            i += 1

        return res

    @classmethod
    def ksys2num(cls, arr, k):
        length = len(arr)
        res = 0
        for i in range(length):
            res += arr[i] * pow(k, i)

        return res

    @classmethod
    def process(cls, arr, k):
        e0 = [0 for _ in range(32)]
        for i in arr:
            cls.execute(e0, i, k)
        res = cls.ksys2num(e0, k)
        return res

    @classmethod
    def execute(cls, e0, value, k):
        cur_ksys = cls.num2ksys(value, k)
        for i in range(len(e0)):
            e0[i] = (e0[i] + cur_ksys[i]) % k


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 6, 6, 2, 2, 10, 10, 10, 12, 12, 12, 6, 9]
    print(KGetter.process(arr, 3))