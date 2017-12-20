"""
给定一个整数N，求由"0"字符与"1"字符组成的长度为N的所有字符串中，满足"0"字符的左边
必有"1"字符的字符串数量。

举例：
N=1。只由"0"和"1"组成，长度为1的所有字符串："0"、"1"。只有字符串"1"满足要求，所以
返回1。
N=2。只由"0"和"1"组成，长度为2的所有字符串为："00"、"01"、"10"、"11"。只有字符串
"10"和"11"满足要求，所以返回2。
N=3。只由"0"和"1"组成，长度为3的所有字符串为："000"、"001"、"010"、"011"、"100"、
"101"、"110"、"111"。字符串"101"、"110"、"111"满足要求，所以返回3。
"""


class BinaryStrHanlder:
    @classmethod
    def get_num_by_recurise(cls, n):
        if not n:
            return 0
        return cls.process(1, n)

    @classmethod
    def process(cls, i, n):
        if i == n:
            return 1
        elif i == n - 1:
            return 2
        else:
            return cls.process(i+1, n) + cls.process(i+2, n)

    @classmethod
    def get_num(cls, n):
        if n < 3:
            return n
        i = 3
        pre_pre_total = 1
        pre_total = 2
        total = pre_pre_total + pre_total
        while i < n:
            tmp = total
            pre_pre_total = pre_total
            pre_total = tmp
            total = pre_total + pre_pre_total
            i += 1

        return total


if __name__ == '__main__':
    for i in range(20):
        print(BinaryStrHanlder.get_num_by_recurise(i))
        print(BinaryStrHanlder.get_num(i))