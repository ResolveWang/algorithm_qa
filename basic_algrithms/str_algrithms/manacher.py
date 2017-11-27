"""
Manacher算法
"""


import sys


class Manacher:
    @classmethod
    def get_max_length(cls, str1):
        if not str1:
            return 0

        my_str = cls.get_manacher_str(str1)
        center = -1
        right = -1
        parr = [0 for _ in range(len(my_str))]
        max_value = -sys.maxsize
        for i in range(len(my_str)):
            if i > right:
                parr[i] = 1
            else:
                parr[i] = min([parr[2*center-i], right-i])
            while i - parr[i] > -1 and i + parr[i] < len(my_str):
                if my_str[parr[i]+i] == my_str[i-parr[i]]:
                    parr[i] += 1
                else:
                    break

            if i + parr[i] > right:
                right = i + parr[i]
                center = i
            max_value = max([max_value, parr[i]])

        return max_value - 1

    @classmethod
    def get_manacher_str(cls, str1):
        new_str = '#'
        for s in str1:
            new_str += '{}#'.format(s)

        return new_str


if __name__ == '__main__':
    str1 = "abc1234321ab"
    print(Manacher.get_max_length(str1))