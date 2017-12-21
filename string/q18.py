"""
问题描述：给定一个字符串str，返回str的最长无重复字符子串的长度。

举例：
str="abcd"，返回4
str="aabcb"，最长无重复字符子串为"abc"，返回3

要求：
如果str的长度为N,请实现时间复杂度为O(N)的方法。
"""


class LongestNotRepeatStr:
    @classmethod
    def get_longest_sut_str(cls, strs):
        if not strs:
            return ''

        pre = -1
        max_length = 0
        str_map = {i: -1 for i in strs}

        i = 0
        while i < len(strs):
            pre = max([pre, str_map[strs[i]]])
            cur_length = i - pre
            max_length = max([max_length, cur_length])
            str_map[strs[i]] = i
            i += 1

        return max_length


if __name__ == '__main__':
    my_str = 'kqetrpslqrpbbdmjvjba'
    print(LongestNotRepeatStr.get_longest_sut_str(my_str))