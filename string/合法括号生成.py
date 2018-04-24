"""
问题: 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
["((()))", "(()())", "(())()", "()(())", "()()()"]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return list()

        res = list()
        self.process(n, n, '', res)
        return res

    def process(self, left, right, cur_str, res):
        if left == 0 and right == 0:
            res.append(cur_str)
        elif left == 0 and right != 0:
            self.process(left, right - 1, cur_str + ')', res)
        elif left != 0 and right == 0:
            return
        elif left < 0 or right < 0:
            return
        elif right == left:
            self.process(left - 1, right, cur_str + '(', res)
        elif right > left:
            self.process(left - 1, right, cur_str + '(', res)
            self.process(left, right - 1, cur_str + ')', res)


