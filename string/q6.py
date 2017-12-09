"""
问题描述：给定三个字符串str、frome和to，已知from字符串中无重复字符，把str中
所有from的子串全部替换成to字符串，对连续出现from的部分要求只替换成一个to字符串，
返回最终的结果字符串。

举例：
str='123abc',from='abc',to='4567',返回'1234567'
str='123',from='abc',to='456',返回'123'
str='123abcabc', from='abc',to='X'，返回'123X'
"""


class StrReplacer:
    @classmethod
    def replace_str(cls, str1, str_from, str_to):
        if not str_from or not str1 or str_from not in str1:
            return str1

        length = len(str1)
        length_from = len(str_from)
        i = 0
        pre_happend = 0
        res = list()
        while i < length:
            count = 0
            while count < length_from and i+count < length and str1[i+count] == str_from[count]:
                count += 1
            # 这里判断是否完全匹配，不完全匹配则将下标右移一位
            if count != length_from:
                pre_happend = 0
                res.append(str1[i])
                i += 1
            else:
                i += count
                if pre_happend:
                    pass
                else:
                    res.append(str_to)
                    pre_happend = 1

        return ''.join(res)


if __name__ == '__main__':
    str1 = "abc1abcabc1234abcabcabc5678"
    str1_from = "abc"
    str1_to = "XXXXX"
    print(StrReplacer.replace_str(str1, str1_from, str1_to))

    str2 = "abc"
    str2_from = "123"
    str2_to = "X"
    print(StrReplacer.replace_str(str2, str2_from, str2_to))