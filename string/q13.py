"""
问题描述：给定一个字符串str，如果可以在str的任意位置添加字符，请返回在添加字符最少的情况下，让str整体都是
回文字符串的一种结果。

举例：
str='ABA',str本身就是回文串，不需要添加字符，所以返回'ABA'.
str='AB'，可以在'A'之前添加'B'，使str整体都是回文串，故可以返回'BAB'。也可以在'B'之后添加'A'，使str整
体都是回文串，故也可以返回'ABA'，总之，只要添加的字符数最少，只返回其中一种结果即可。

进阶题目：
给定一个字符串str，再给定str的最长回文子序列字符串strlps，请返回在添加字符最少的情况下，让str整体都是回文
字符串的一种结果。进阶问题比原问题多了一个参数，请做到时间复杂度比原问题的实现低。

举例：
str='A1B21C',strlps='121'，返回'AC1B2B1CA'或者'CA1B2B1AC'。总之，只要是添加的字符数最少，只返回其
中一种结果即可。
"""


class Palindrome:
    @classmethod
    def get_dp(cls, strs):
        length = len(strs)
        dp = [[0 for _ in strs] for _ in strs]
        j = 1
        while j < length:
            dp[j-1][j] = 0 if strs[j-1] == strs[j] else 1
            i = j - 2
            while i > -1:
                if strs[i] == strs[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min([dp[i][j-1], dp[i+1][j]]) + 1
                i -= 1
            j += 1
        return dp

    @classmethod
    def get_smallest_palindrome(cls, strs):
        if not strs or len(strs) == 1:
            return strs

        dp = cls.get_dp(strs)
        new_chars = ['' for _ in range(dp[0][len(strs)-1] + len(strs))]
        i = 0
        j = len(strs) - 1
        resl = 0
        resr = len(new_chars) - 1
        while i <= j:
            if strs[i] == strs[j]:
                new_chars[resl] = strs[i]
                new_chars[resr] = strs[j]
                i += 1
                j -= 1
                resl += 1
                resr -= 1
            elif dp[i][j-1] < dp[i+1][j]:
                new_chars[resl] = strs[j]
                new_chars[resr] = strs[j]
                j -= 1
                resl += 1
                resr -= 1
            else:
                new_chars[resl] = strs[i]
                new_chars[resr] = strs[i]
                i += 1
                resl += 1
                resr -= 1

        return ''.join(new_chars)

    @classmethod
    def get_smallest_palindrome_by_lps(cls, strs, strlps):
        if not strs or len(strs) == 1:
            return strs

        strsl = 0
        strsr = len(strs) - 1
        lpsl = 0
        lpsr = len(strlps) - 1
        new_chars = ['' for _ in range(2 * len(strs) - len(strlps))]
        charsl = 0
        charsr = len(new_chars) - 1
        templ = 0
        templr = len(strs)
        while lpsl <= lpsr:
            while strlps[lpsl] != strs[strsl]:
                strsl += 1
            left_part = strs[templ:strsl]

            templ = strsl + 1

            while strlps[lpsr] != strs[strsr]:
                strsr -= 1

            right_part = strs[strsr+1:templr]
            templr = strsr
            joined_part = left_part + right_part

            for i in joined_part:
                new_chars[charsl] = i
                new_chars[charsr] = i
                charsl += 1
                charsr -= 1
            new_chars[charsl] = strs[strsl]
            new_chars[charsr] = strs[strsl]
            charsl += 1
            charsr -= 1

            lpsl += 1
            lpsr -= 1

        return ''.join(new_chars)


if __name__ == '__main__':
    my_str = "AB1CD2EFG3H43IJK2L1MN"
    print(Palindrome.get_smallest_palindrome(my_str))
    print(Palindrome.get_smallest_palindrome_by_lps(my_str, '1234321'))