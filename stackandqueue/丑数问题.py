"""
编写一个程序，找出第 n 个丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。

示例:
n = 10 => 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:
1 是丑数。
n 不超过1690。
"""


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        if n == 1:
            return 1

        l1 = [2]
        l2 = [3]
        l3 = [5]

        cur = 1
        count = 1

        s1 = {2}
        s2 = {3}

        while count < n:
            cur = min([l1[0], l2[0], l3[0]])
            if cur == l1[0]:
                l1.pop(0)
                if cur * 2 not in s1:
                    s1.add(cur * 2)
                    l1.append(cur * 2)
                if cur * 3 not in s1:
                    s1.add(cur * 3)
                    l1.append(cur * 3)
                if cur * 5 not in s1:
                    s1.add(cur * 5)
                    l1.append(cur * 5)
                l1.sort()
            elif cur == l2[0]:
                l2.pop(0)
                if cur * 3 not in s2:
                    s2.add(cur * 3)
                    l2.append(cur * 3)
                if cur * 5 not in s2:
                    s2.add(cur * 5)
                    l2.append(cur * 5)

                l2.sort()
            elif cur == l3[0]:
                l3.pop(0)
                l3.append(cur * 5)
            count += 1

        return cur
