"""
问题描述：给定一个整数N，如果N<1，代表空树结构，否则代表中序遍历的结果为{1, 2, 3, ..., N}。
请返回可能的二叉树结构有多少。

例如，N=-1时，代表空树结构，返回1；N=2时，满足中序遍历为{1， 2}的二叉树结构只有两种结构，所以
结果返回为2
"""


class TreeFromInt:
    @classmethod
    def get_total_num(cls, n):
        if n < 2:
            return 1

        total = 0
        for i in range(1, n+1):
            total += cls.get_tree_num_from_int(n, i)

        return total

    @classmethod
    def get_tree_num_from_int(cls, n, i):
        if i == 1:
            return cls.get_total_num(n-1)
        if i == n:
            return cls.get_total_num(n-1)
        return cls.get_total_num(i-1) * cls.get_total_num(n-i)


if __name__ == '__main__':
    n = 4
    print(TreeFromInt.get_total_num(n))