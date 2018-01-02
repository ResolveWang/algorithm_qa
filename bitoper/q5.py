"""
问题描述:给定一个整型数组arr,其中只有一个数出现了奇数次，其它的数都出现了偶数次，
打印这个数。

进阶：有两个数出现了奇数次，其他的数都出现了偶数次，打印这两个数。

要求：
时间复杂度为O(N)，额外空间复杂度为O(1).
"""


class OddFinder:
    @classmethod
    def find_one_odd(cls, arr):
        flag = 0
        for i in arr:
            flag ^= i

        return flag

    @classmethod
    def find_two_odd(cls, arr):
        pass


if __name__ == '__main__':
    a = [1, 1, 2, 2, 5, 4, 4, 7, 7, 7, 7]
    b = [1, 1, 2, 2, 5, 4, 4, 7, 7, 7, 7, 3, 3, 3]
    print(OddFinder.find_one_odd(a))