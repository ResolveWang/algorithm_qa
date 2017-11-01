"""
问题描述：给定整数N，返回斐波那契数列的第N项

补充题目：给定整数N，代表台阶数，一次可以跨2个或者1个台阶，返回有多少种走法。

补充题目2：假设农场中成熟的母牛每年会生一头小母牛，而且永远不会死。第一年农场有1只成熟的母牛，从第二年开始，
母牛开始生小母牛。每只小母牛3年之后成熟又可以生小母牛。给定整数N，求出N年后牛的数量。

要求：对以上所有问题，实现时间复杂度为O(logN)的解法
"""

# 由于数学能力和理解能力有限，这里给出O(N)的解法

class FBNZ:
    @classmethod
    def classic_question(cls, n):
        if n < 1:
            return 0

        if n == 1 or n == 2:
            return 1

        cur = 1
        pre = 1
        pos = 3

        while pos <= n:
            temp = cur
            cur = pre + cur
            pre = temp
            pos += 1

        return cur

    @classmethod
    def jump_tj(cls, n):
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return n
        cur = 2
        pre = 1
        pos = 3

        while pos <= n:
            temp = cur
            cur = pre + cur
            pre = temp
            pos += 1

        return cur

    @classmethod
    def cow_count(cls, n):
        if n < 1:
            return 0

        if n == 1 or n == 2 or n == 3:
            return n

        cur = 3
        pre = 2
        prepare = 1
        pos = 4

        while pos <= n:
            temp1 = cur
            temp2 = pre
            cur = prepare + cur
            pre = temp1
            prepare = temp2
            pos += 1
        return cur


if __name__ == '__main__':
    assert FBNZ.classic_question(20) == 6765
    assert FBNZ.jump_tj(20) == 10946
    assert FBNZ.cow_count(20) == 1873