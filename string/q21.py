"""
问题描述:给定一个字符串str，返回把str全部切成回文子串的最小分割数。
举例:
str="ABA"
不需要切割，str本身就是回文串。所以返回0.
str="ACDCDCDAD"
最少需要切２次变成３个回文子串，比如"A"、"CDCDC"和"DAD"，所以返回２.
"""
import sys


class PalindromeMincut:
    @classmethod
    def get_min_cut(cls, strs):
        if not strs:
            return 0

        length = len(strs)
        dp = [0 for _ in range(length+1)]
        dp[length] = -1
        is_palindrome = [[False for _ in range(length)] for _ in range(length)]

        i = length - 1
        while i >= 0:
            dp[i] = sys.maxsize
            j = i
            while j < length:
                if strs[i] == strs[j] and (j - i < 2 or is_palindrome[i+1][j-1]):
                    dp[i] = min([dp[i], dp[j+1]+1])
                    is_palindrome[i][j] = True
                j += 1
            i -= 1

        return dp[0]


if __name__ == '__main__':
    strs = 'CCDBABDB'
    print(PalindromeMincut.get_min_cut(strs))