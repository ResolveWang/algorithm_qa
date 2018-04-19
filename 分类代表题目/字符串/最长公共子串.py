"""
问题: 对于两个字符串，请设计一个时间复杂度为O(m*n)的算法(这里的m和n为两串的长度)，求出两串的最长公共子串
的长度。这里的最长公共子串的定义为两个序列U1,U2,..Un和V1,V2,...Vn，其中Ui + 1 == Ui+1,
Vi + 1 == Vi+1，同时Ui == Vi。给定两个字符串A和B，同时给定两串的长度n和m。
"""


class LongestSubstring:
    def findLongest(self, A, n, B, m):
        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if A[i] == B[0]:
                dp[0][i] = 1

        for i in range(m):
            if A[0] == B[i]:
                dp[i][0] = 1

        max_length = 0
        for row in range(1, m):
            for col in range(1, n):
                if B[row] == A[col]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                    max_length = max([max_length, dp[row][col]])
                else:
                    dp[row][col] = 0
        return max_length


if __name__ == '__main__':
    solution = LongestSubstring()
    print(solution.findLongest("1AB2345CD", 9, "12345EF", 7))