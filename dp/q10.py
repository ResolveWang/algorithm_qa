"""
问题描述：给定三个字符串str1、str2和aim,如果aim包含且仅包含来自str1和str2的所有字符，
而且在aim中属于str1的字符之间保持原来在str1中的顺序，属于str2的字符之间保持原来在str2
中的顺序，那么称aim是str1和str2的交错组成。实现一个函数，判断aim是否是str1和str2的交
错组成。

举例AB
str1="",str2="12"，那么"AB12"、"A1B2"、"A12B"、"1A2B"和"1AB2"等都是str1和str2
的交错组成。
"""


class CrossStr:
    @classmethod
    def is_cross_str(cls, str1, str2, aim):
        if not str1 or not str2 or not aim:
            return False

        str_len1 = len(str1)
        str_len2 = len(str2)
        aim_len = len(aim)

        if str_len1 + str_len2 != aim_len:
            return False

        dp = [[False for _ in range(str_len2+1)] for _ in range(str_len1+1)]
        dp[0][0] = True

        for i in range(1, str_len1+1):
            if aim[i-1] == str1[i-1]:
                dp[i][0] = True

        for j in range(1, str_len2+1):
            if aim[j-1] == str2[j-1]:
                dp[0][j] = True

        for i in range(1, str_len1+1):
            for j in range(1, str_len2+1):
                if dp[i-1][j] and aim[i+j-1] == str1[i-1]:
                    dp[i][j] = True
                elif dp[i][j-1] and aim[i+j-1] == str2[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

        return dp[str_len1][str_len2]


if __name__ == '__main__':
    str1 = "1234"
    str2 = "abcd"
    aim = "1a23bcd4"
    print(CrossStr.is_cross_str(str1, str2, aim))