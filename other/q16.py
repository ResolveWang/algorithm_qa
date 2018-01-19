"""
给定一个整数n,返回从1到n的数字中1个出现的个数.
例如:
n=5,1~n为1,2,3,4,5.那么1出现了1次,所以返回1.
n=11,1~n为1,2,3,4,5,6,7,8,9,10,11.那么1出现的次数为1(出现
1次),10(出现1次),11(有两个1,所以出现了2次),所以返回4
"""


class OneCounter:
    @classmethod
    def get_nums_of_one(cls, n):
        if n == 0:
            return 0

        n = abs(n)

        high_pos = 1
        cur = 9
        while cur/n < 1:
            cur = 9 * pow(10, high_pos) + cur
            high_pos += 1

        return cls.process(n, high_pos)

    @classmethod
    def process(cls, n, pos):
        if n < 10:
            return 1
        left = int(n % pow(10, pos-1))
        num = int(n/pow(10, pos-1))
        if num > 1:
            first_one_num = pow(10, pos-1)
        else:
            first_one_num = n - num * pow(10, pos-1) + 1

        other_one_num = num * (pos-1) * (pow(10, pos-1)/10)
        return int(first_one_num + other_one_num + cls.process(left, pos-1))


if __name__ == '__main__':
    print(OneCounter.get_nums_of_one(9991))
