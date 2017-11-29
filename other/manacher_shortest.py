"""
问题描述：给定一个字符串str1，只能往str1的后面添加字符变成str2，要求str2
整体都是回文串且最短。

举例：
str1 = ABC12321，则返回ABC12321CBA
"""

import sys


class ShortestEnd:
    @classmethod
    def get_shortest_end_by_manacher(cls, str1):
        if not str1:
            return ''

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

            if right == len(my_str):
                max_value = parr[i]
                break
        return str1 + str1[:len(str1)+1-max_value][::-1]

    @classmethod
    def get_manacher_str(cls, str1):
        new_str = '#'
        for s in str1:
            new_str += '{}#'.format(s)

        return new_str


if __name__ == '__main__':
    my_str = 'abcd12321'
    print(ShortestEnd.get_shortest_end_by_manacher(my_str))