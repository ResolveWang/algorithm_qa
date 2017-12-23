"""
问题描述：给定字符串str，其中绝对不含有字符"."和"*"。再给定字符串
exp，其中可以含有'.'或者'*'，'*'字符不能是exp的首字符，并且任意两
个字符不相邻。exp中的"."代表任何一个字符，exp中的'*'表示'*'的前一个
字符可以有0个或者多个。请写一个函数，判断str是否能被exp匹配.

举例:
str="abc"，exp="abc"，返回true
str="abc"，exp="a.c"，exp中单个'.'可以代表任意字符，所以返回true
str='abcd'，exp='.*'，exp中'*'的前一个字符是","，所以可表示任意数量
的"."字符，当exp是"..."时与"abcd"匹配，返回true
str="",exp="..*"。exp中"*"的前一个字符是"."，可表示任意数量的"."字符，
但是".*"之前还有一个'.'字符，该字符不受'*'影响，所以str起码有一个字符才
能被exp匹配，所以返回false.
"""


class RegularExpressionMath:
    @classmethod
    def is_valid(cls, s, e):
        if '.' in s or '*' in s:
            return False
        if '**' in e or e[0] == '*':
            return False
        return True

    @classmethod
    def is_match(cls, s, e):
        if not s or not e:
            return False

        if not cls.is_valid(s, e):
            return False

        return cls.process(s, e, 0, 0)

    @classmethod
    def process(cls, s, e, si, ei):
        if ei == len(e):
            return si == len(s)

        if ei + 1 == len(e) or e[ei+1] != '*':
            return si != len(s) and (e[ei] == s[si] or e[ei] == '.') and \
                   cls.process(s, e, si+1, ei+1)

        while si != len(s) and (e[ei] == s[si] or e[ei] == '.'):
            if cls.process(s, e, si, ei+2):
                return True
            si += 1

        return cls.process(s, e, si, ei+2)

    @classmethod
    def init_map(cls, s, e):
        s_len = len(s)
        e_len = len(e)
        dp = [[False for _ in range(e_len+1)] for _ in range(s_len+1)]
        dp[s_len][e_len] = True

        j = e_len - 2
        while j >= 0:
            if e[j] != '*' and e[j+1] == '*':
                dp[s_len][j] = True
            else:
                break
            j -= 1

        if e[e_len-1] == '.' or e[e_len-1] == s[s_len-1]:
            dp[s_len-1][e_len-1] = True
        return dp

    @classmethod
    def is_match_by_dp(cls, s, e):
        if not s or not e:
            return False

        if not cls.is_valid(s, e):
            return False

        dp = cls.init_map(s, e)
        i = len(s) - 1
        while i >= 0:
            j = len(e) - 2
            while j >= 0:
                if e[j+1] != '*':
                    dp[i][j] = (s[i] == e[j] or e[j] == '.') and dp[i+1][j+1]
                else:
                    si = i
                    while si != len(s) and (s[si] == e[j] or e[j] == '.'):
                        if dp[si][j+2]:
                            dp[i][j] = True
                            break
                        si += 1

                    if not dp[i][j]:
                        dp[i][j] = dp[si][j+2]
                j -= 1
            i -= 1
        return dp[0][0]


if __name__ == '__main__':
    strs = "abcccdefg"
    exp = "ab.*d.*e.*"
    print(RegularExpressionMath.is_match(strs, exp))
    print(RegularExpressionMath.is_match_by_dp(strs, exp))

