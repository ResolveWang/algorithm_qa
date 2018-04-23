"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3.注意空字符串可被认为是有效字符串。

比如: "()" => true   "()[]{}" => true  "([)]" => false "{[]}" => true
"""


class Solution:
    def isValid(self, s):
        if not s:
            return True

        if len(s) & 1 == 1:
            return False

        sign_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        help_stack = list()
        index = 0
        while index < len(s):
            if s[index] in sign_map.values():
                help_stack.append(s[index])
            else:
                if not help_stack:
                    return False
                tmp = help_stack.pop()
                if tmp != sign_map.get(s[index]):
                    return False
            index += 1

        return True if not help_stack else False
