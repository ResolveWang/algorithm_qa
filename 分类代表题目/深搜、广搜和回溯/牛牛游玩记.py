"""
问题: 又是晴朗的一天，牛牛的小伙伴们都跑来找牛牛去公园玩。但是牛牛想呆在家里看E3展，不想出去逛公园，
可是牛牛又不想鸽掉他的小伙伴们，于是找来了公园的地图，发现公园是由一个边长为n的正方形构成的，公园
一共有m个入口，但出口只有一个。公园内有一些湖和建筑，牛牛和他的小伙伴们肯定不能从他们中间穿过，所以
只能绕行。牛牛想知道他需要走的最短距离并输出这个最短距离。

输入:
第一行输入一个数字n(1≤n≤1000)表示公园的边长
接下来会给你一个n*n的公园地图，其中 . 表示公园里的道路，@表示公园的入口，*表示公园的出口，#表示公园
内的湖和建筑。牛牛和他的小伙伴们每次只能上下左右移动一格位置。输入保证公园入口个数m(1≤m≤10000)且所
有的入口都能和出口相连。

输出描述:
输出牛牛需要行走的最短距离。

示例

输入：
10
.@....##@.
......#...
...@..#...
###.......
....##..#.
...####...
@...##....
#####.....
..##*####.
#.........

输出:
16
"""


class Node:
    def __init__(self):
        self.x = None
        self.y = None


class ShortPath:
    def get_shortest_path(self, matrix):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        q = list()
        ed = Node()
        dis = [[-1 for _ in range(1005)] for _ in range(1005)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '*':
                    ed.x = i
                    ed.y = j
                    dis[i][j] = 0
                    q.append(ed)
                    break

        while q:
            p = q.pop(0)
            for i in range(4):
                px = p.x + dx[i]
                py = p.y + dy[i]
                if dis[px][py] == -1 and 0 <= px < len(matrix) and 0 <= py < len(matrix) and matrix[px][py] != '#':
                    pp = Node()
                    pp.x = px
                    pp.y = py
                    q.append(pp)
                    dis[px][py] = dis[p.x][p.y] + 1
                    if matrix[px][py] == '@':
                        print(dis[px][py])
                        return


if __name__ == '__main__':
    n = int(input().strip())
    mat = list()
    for _ in range(n):
        values = input().strip()
        mat.append(values)
    s = ShortPath()
    s.get_shortest_path(mat)