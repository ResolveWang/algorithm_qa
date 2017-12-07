"""
问题描述：给定一个字符串str，求其中全部数字串所代表的数字之和。

要去：
1. 忽略小数点字符串，例如"A1.3"，其中包含两个数字1和3
2. 如果紧贴数字子串的左侧出现字符"-"，当连续出现的数量为奇数时，
则数字视为负，连续出现的数量为偶数的时候，则数字视为正。例如，"A-1BC--12",
其中包含数字为-1和12

举例：
str="A1CD2E33"，返回36.
str="A-1B--2C--D6E"，返回7
"""


class SumOfStr:
    @classmethod
    def get_sum(cls, str1):
        str_sum = 0
        length = len(str1)
        index = 0
        while index < length:
            flag = 0
            if str1[index].isdecimal():
                str_sum, index = cls.get_longest_num(str1, index, str_sum, flag)
            else:
                if str1[index] == '-':
                    flag += 1
                    end = index + 1
                    while end < length:
                        if str1[end] == '-':
                            flag += 1
                            end += 1
                        elif str1[end].isdecimal():
                            str_sum, index = cls.get_longest_num(str1, end, str_sum, flag)
                            break
                        else:
                            flag = 0
                            index = end
                            break
            index += 1
        return str_sum

    @classmethod
    def get_longest_num(cls, str1, index, str_sum, flag):
        end = index + 1
        while end < len(str1) and str1[end].isdecimal():
            end += 1
        if flag % 2 == 0:
            str_sum += int(str1[index:end])
        else:
            str_sum -= int(str1[index:end])

        # end是下一个该检查的位置，但是需要判断end是否到达末尾
        return str_sum, end - 1


if __name__ == '__main__':
    print(SumOfStr.get_sum('1K-100ABC500D-T--100F200G!!100H---300'))