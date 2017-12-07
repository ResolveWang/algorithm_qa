"""
问题描述：给定一个字符串str和一个整数k,如果str中正好有连续的K个'0'字符出现时，
把连续的'0'字符去除，返回处理后的字符串。

举例：
str='A00B',k=2, 返回'AB'
str='0000A0000B00C000D0000',k=4,返回'AB00C000D'
"""


class SubStr:
    @classmethod
    def get_sub_str(cls, str1, k):
        i = 0
        length = len(str1)
        count = 0
        while i < length:
            temp = i
            while temp < length and str1[temp] == '0':
                count += 1
                temp += 1
            temp = i
            i += count
            if count == k:
                str1 = str1[0:temp]+'~'*k+str1[temp+k:]
            i += 1
            count = 0

        return str1


if __name__ == '__main__':
    print(SubStr.get_sub_str('A00B', 2))
    test4 = "0000A0000B00C000D0000"
    print(SubStr.get_sub_str(test4, 4))