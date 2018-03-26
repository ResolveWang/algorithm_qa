"""
问题描述:给你一根长度为n的绳子,请把绳子剪成m段(m,n都是整数，m>1并且n>1)，每段
绳子的长度记为k[0],k[1]...k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多
少？例如，当绳子长度为8时，我们把它剪成长度为2,3,3的三段，此时得到的最大乘积为18
"""


class Solution:
    def cut(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        arr = [0 for _ in range(n+1)]
        arr[1] = 1
        arr[2] = 2
        arr[3] = 3

        for i in range(4, n+1):
            max_val = 0
            for j in range(1, i):
                max_val = max([max_val, arr[i-j]*arr[j]])
            arr[i] = max_val

        return arr[n]

    def recursive(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1

        if n == 3:
            return 2

        return self.process(n)

    def process(self, n):
        if n < 4:
            return n
        max_val = 0
        for i in range(1, n):
            max_val = max([self.process(n-i) * self.process(i), max_val])

        return max_val


if __name__ == '__main__':
    print(Solution().cut(8))
    print(Solution().recursive(8))