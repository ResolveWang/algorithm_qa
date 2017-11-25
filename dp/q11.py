"""
给定一个二维数组map，含义是一张地图，例如，如下矩阵：
-2 -3 3
-5 -10 1
0 30 -5

游戏规则如下：
（1）骑士从左上角出发，每次只能向右或者向下走，最后到达右下角见到公主。
（2）地图中每个位置的值代表骑士要遭遇的事情。如果是负数，说明此处有怪兽，
要让骑士掉血。如果是非负数，则代表此处有血瓶，能让骑士回血。
（3）骑士从左上角到右下角的过程中，走到任何一个位置，血量都不能少于1.

为了保证骑士能见到公主，初始血量至少是多少？根据map，返回初始血量。
"""


class DungenonGame:
    @classmethod
    def get_min_hp(cls, m):
        if not m:
            return 1

        len1 = len(m)
        len2 = len(m[0])
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        dp[len1-1][len2-1] = 1 if m[len1-1][len2-1] >= 0 else -m[len1-1][len2-1] + 1
        for rows in range(len1-2, -1, -1):
            dp[rows][len2-1] = max([dp[rows+1][len2-1]-m[rows][len2-1], 1])
            rows += 1

        for cols in range(len2-2, -1, -1):
            dp[len1-1][cols] = max([dp[len1-1][cols+1]-m[len1-1][cols], 1])
            cols += 1
        for rows in range(len1-2, -1, -1):
            for cols in range(len2 - 2, -1, -1):
                down = max(dp[rows+1][cols]-m[rows][cols], 1)
                right = max(dp[rows][cols+1]-m[rows][cols], 1)
                dp[rows][cols] = min(down, right)

        return dp[0][0]


if __name__ == '__main__':
    my_map = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(DungenonGame.get_min_hp(my_map))