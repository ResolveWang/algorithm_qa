"""
问题描述：给定两个字符串str1和str2，返回两个字符串的最长公共子序列。
举例：
str1="1A2C3D4B56", str2="B1D23CA45B6A"。
"123456"或者"12C4B6"都是最长公共子序列，返回哪一个都行。
"""


class SubSeqFinder:
    @classmethod
    def get_dp(cls, str1, str2):
        str_len1 = len(str1)
        str_len2 = len(str2)

        dp = [[0 for _ in range(str_len2)] for _ in range(str_len1)]
        flag = False
        for col in range(str_len2):
            if flag == 1:
                dp[0][col] = 1
                continue

            if str1[0] == str2[col]:
                dp[0][col] = 1
                flag = 1

        flag = 0 if flag == 1 else 0
        for row in range(str_len1):
            if flag == 1:
                dp[row][0] = 1
                continue

            if str1[row] == str2[0]:
                dp[row][0] = 1
                flag = 1

        for row in range(1, str_len1):
            for col in range(1, str_len2):
                dp[row][col] = max([dp[row-1][col], dp[row][col-1]])
                if str1[row] == str2[col]:
                    dp[row][col] = max([dp[row][col], dp[row-1][col-1] + 1])
        return dp

    @classmethod
    def get_max_subsuquence(cls, str1, str2):
        if not str1 or not str2:
            return str1 if not str1 else str2

        dp = cls.get_dp(str1, str2)
        row = len(str1) - 1
        col = len(str2) - 1
        index = dp[row][col] - 1
        res = []

        while index >= 0:
            if col > 0 and dp[row][col] == dp[row][col-1]:
                col -= 1
            elif row > 0 and dp[row][col] == dp[row-1][col]:
                row -= 1
            else:
                res.insert(0, str1[row])
                row -= 1
                col -= 1
                index -= 1

        return res


if __name__ == '__main__':
    str1 = "1A2C3D4B56"
    str2 = "B1D23CA45B6A"
    print(SubSeqFinder.get_max_subsuquence(str1, str2))