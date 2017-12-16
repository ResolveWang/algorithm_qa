"""
问题描述：给定字符串str，判断是不是整体有效的括号字符串。
举例：
str="()"，返回true;str="(()())",返回true;str="(())"，返回true.
str="(()"，返回false;str="()(",返回false;str="()a()"，返回false.

补充题目：
给定一个括号字符串str，返回最长的有效括号子串。
举例：
str="(()())",返回6；str="())"，返回2;str="()(()()(",返回4。
"""


class ParenthesesProblem:
    @classmethod
    def is_valid(cls, strs):
        if not strs or len(strs) == 1:
            return False

        length = len(strs)
        i = 0
        left_count = 0
        right_count = 0
        while i < length:
            if strs[i] != '(' and strs[i] != ')':
                return False

            if strs[i] == '(':
                left_count += 1
            else:
                right_count += 1

            if left_count < right_count:
                return False

            i += 1

        if left_count != right_count:
            return False

        return True

    @classmethod
    def get_max_length(cls, strs):
        if not strs or len(strs) == 1:
            return 0

        res = 0
        length = len(strs)
        dp = [0 for _ in range(length)]
        i = 0
        while i < length:
            if strs[i] == ')':
                pre = i - dp[i-1] - 1
                if pre >= 0 and strs[pre] == '(':
                    dp[i] = dp[i-1] + 2
                    if pre > 0:
                        dp[i] = dp[i] + dp[pre-1]
            res = max([res, dp[i]])
            i += 1
        return res


if __name__ == '__main__':
    str1 = '((())())'
    print(ParenthesesProblem.is_valid(str1))
    print(ParenthesesProblem.get_max_length(str1))

    str2 = '(())(()(()))'
    print(ParenthesesProblem.is_valid(str2))
    print(ParenthesesProblem.get_max_length(str2))

    str3 = '()(()()('
    print(ParenthesesProblem.is_valid(str3))
    print(ParenthesesProblem.get_max_length(str3))