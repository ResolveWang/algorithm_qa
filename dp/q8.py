"""
问题描述：给定两个字符串str1和str2，返回两个字符串的最长公共子串。

举例
str1="1AB2345CD", str2="12345EF", 返回2345

要求
如果str1长度为M，str2长度为N，实现时间复杂度为O(M*N)，额外空间复杂度为O(1)的方法。
"""


class MaxSubPubstrFinder:
    @classmethod
    def get_max_common_length(cls, str1, str2):
        str_len1 = len(str1)
        str_len2 = len(str2)

        dp = [[0 for _ in range(str_len2)] for _ in range(str_len1)]

        for i in range(str_len1):
            if str1[i] == str2[0]:
                dp[i][0] = 1

        for j in range(str_len2):
            if str2[j] == str1[0]:
                dp[0][j] = 1

        for i in range(1, str_len1):
            for j in range(1, str_len2):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return dp

    @classmethod
    def get_max_common_str(cls, str1, str2):
        if not str1 or not str2:
            return ''

        dp = cls.get_max_common_length(str1, str2)

        max_length = 0
        row = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    row = i

        return str1[row-max_length+1:row+1]


if __name__ == '__main__':
    str1 = "1AB2345CD"
    str2 = "12345EF"
    print(MaxSubPubstrFinder.get_max_common_str(str1, str2))