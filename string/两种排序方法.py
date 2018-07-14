"""
问题描述: 考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法:
1.根据字符串的字典序排序。例如：
"car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如：
"car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。
输入描述:
输入第一行为字符串个数n(n ≤ 100)
接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成

输出描述:
如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",
如果根据长度排列而不是字典序排列输出"lengths",
如果两种方式都符合输出"both"，否则输出"none"

输入例子1:
3
a
aa
bbb

输出例子1:
both
"""


import sys


class Solution:
    def get_satisfied_methods(self, arr):
        if len(arr) <= 1:
            print('both')
            return

        by_length = True
        by_lex = True
        index = 1
        pre = arr[0]
        while index < len(arr):
            if len(arr[index]) < len(pre):
                by_length = False

            if arr[index] < pre:
                by_lex = False

            if not by_length and not by_lex:
                break
            pre = arr[index]
            index += 1

        if by_length and by_lex:
            print('both')
            return
        elif by_length:
            print('lengths')
        elif by_lex:
            print('lexicographically')
        else:
            print('none')


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    inputs = list()
    for _ in range(n):
        inputs.append(sys.stdin.readline().strip())
    s = Solution()
    s.get_satisfied_methods(inputs)