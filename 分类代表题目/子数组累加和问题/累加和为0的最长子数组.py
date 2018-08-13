"""
问题描述: 一个一维维数组中只有1和-1，实现程序，求和为0的最长子串长度

方法: 将sum(i)记录下来，如果i后面的index j 的和也为sum(i)，那么则
它们中间的和必定为0，我们取最大值即可: max(j-i).
为了记录最大的distance，对于相同的sum，我们只记录第一次出现的index
"""


class Solution(object):
    def fun(self, l):
        dic = {}
        total = 0
        max_len = 0
        for x in range(len(l)):
            total += l[x]
            if total in dic:
                max_len = max(max_len, x - dic[total])
            else:
                dic[total] = x
        return max_len


if __name__ == '__main__':
    r = Solution().fun([-1, 1, -1, 1, 1, 1, -1, -1, -1])
    print(r)
