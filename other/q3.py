"""
问题描述:给定一个非负整数N,返回N!结果的末尾为０的数量.
例如:
3!=6,结尾的末尾没有0,返回0. 5!=120,结果的末尾有１个0,返回1.
1000000000!,结果的末尾有249999998个0,返回249999998.

进阶题目:
给定一个非负整数N,如果用二进制数表达N!的结果,返回最低位的1在
哪个位置上,认为最右的位置为位置0.
例如:1!=1,最低位的1在0位置上.2!=2,最低位的1在1位置上.1000000000!,
最低位的1在999999987位置上.
"""


class AssignedNumFinder:
    @classmethod
    def get_0_num(cls, n):
        if n < 0:
            return 0
        res = 0
        i = 5
        while i < n+1:
            cur = i
            while cur % 5 == 0:
                res += 1
                cur = cur / 5

            i += 5

        return res

    @classmethod
    def get_0_nums(cls, n):
        res = 0
        for i in range(1, n+1):
            res += cls.get_0_num(i)

        return res

    @classmethod
    def get_0_nums_best(cls, n):
        biggest_num = 0
        while pow(5, biggest_num) <= n:
            biggest_num += 1

        res = 0
        for i in range(1, biggest_num+1):
            res += int(n/pow(5, i))

        return res

    @classmethod
    def get_1_nums_best(cls, n):
        biggest_num = 0
        while pow(2, biggest_num) <= n:
            biggest_num += 1

        res = 0
        for i in range(1, biggest_num + 1):
            res += int(n / pow(2, i))

        return res


if __name__ == '__main__':
    print(AssignedNumFinder.get_0_nums_best(1000000000))
    print(AssignedNumFinder.get_1_nums_best(1000000000))