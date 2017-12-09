"""
问题描述：给定一个字符串，返回它的统计字符串。比如，"aaabbadddffc"的统计字符串为
"a_3_b_2_a_1_d_3_f_2_c_1".

补充题目：给定一个字符串的统计字符串cstr,再给定一个整数index，返回cstr所代表的原始
字符串上的第index个字符串。例如，"a_1_b_100"所代表的原始字符串上的第0个字符串是'a',
第50个字符串是'b'.
"""


class StrStatistics:
    @classmethod
    def statistics_str(cls, str1):
        if not str1:
            return str1

        length = len(str1)
        i = 0
        res = list()
        while i < length:
            count = 0
            while i + count < length and str1[i+count] == str1[i]:
                count += 1
            res.append('{}_{}'.format(str1[i], count))
            i += count

        return '_'.join(res)

    @classmethod
    def get_char(cls, cstr, k):
        if not cstr:
            return

        res = cstr.split('_')
        index_sum = 0
        i = 1
        while index_sum < k:
            if i > len(res):
                return ''
            index_sum += int(res[i])
            i += 2

        return res[i-1]


if __name__ == '__main__':
    res = StrStatistics.statistics_str('aaabbadddffc')
    print(StrStatistics.get_char(res, 9))