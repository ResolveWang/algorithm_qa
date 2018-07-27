"""
问题描述: 大家一定玩过“推箱子”这个经典的游戏。具体规则就是在一个N*M的地图上，
有1个玩家、1个箱子、1个目的地以及若干障碍，其余是空地。玩家可以往上下左右4个方
向移动，但是不能移动出地图或者移动到障碍里去。如果往这个方向移动推到了箱子，箱子
也会按这个方向移动一格，当然，箱子也不能被推出地图或推到障碍里。当箱子被推到目的
地以后，游戏目标达成。现在告诉你游戏开始是初始的地图布局，请你求出玩家最少需要移
动多少步才能够将游戏目标达成。

输入描述:
每个测试输入包含1个测试用例
第一行输入两个数字N，M表示地图的大小。其中0<N，M<=8。
接下来有N行，每行包含M个字符表示该行地图。其中 . 表示空地、X表示玩家、*表示箱子、
#表示障碍、@表示目的地。
每个地图必定包含1个玩家、1个箱子、1个目的地。

输出描述:
输出一个数字表示玩家最少需要移动多少步才能将游戏目标达成。当无论如何达成不了的时候，输出-1。

示例1
输入
4 4
....
..*@
....
.X..
6 6
...#..
......
#*##..
..##.#
..X...
.@#...

输出
3
11
"""


start = [-1] * 4 # 前两位表示箱子的起始位置，后两位表示玩家的位置
end = [-1] * 2
n, m = map(int, input().split())
mat = list()
for i in range(n):
    line = input()
    mat.append(line)
    for j in range(len(line)):
        # box pos
        if line[j] == '*':
            start[0], start[1] = i, j
        # player pos
        if line[j] == 'X':
            start[2], start[3] = i, j
        # dest pos
        if line[j] == '@':
            end[0], end[1] = i, j

# 四维表用以记录箱子的x,y及玩家的x,y
reach = [[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = list()
queue.append(start)
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
reach[start[0]][start[1]][start[2]][start[3]] = 0
while len(queue):
    cur = queue.pop(0)
    if cur[0] == end[0] and cur[1] == end[1]:
        print(reach[cur[0]][cur[1]][cur[2]][cur[3]])
        break

    # 可以往四个方向推
    for i in range(4):
        player_x = cur[2] + direction[i][0]
        player_y = cur[3] + direction[i][1]

        # 检查箱子和玩家位置是否合法
        if 0 <= player_x < n and 0 <= player_y < m and mat[player_x][player_y] != '#':
            # 检查玩家和箱子是否重合
            if player_x == cur[0] and player_y == cur[1]:
                # 重合的时候将箱子往同一个方向推并检查箱子状态是否合法
                box_x, box_y = cur[0] + direction[i][0], cur[1] + direction[i][1]
                if box_x < 0 or box_x >= n or box_y < 0 or box_y >= m or mat[box_x][box_y] == '#':
                    continue
            else:
                # 如果不重合则箱子位置不动
                box_x, box_y = cur[0], cur[1]
            # 判断该点是否已经遍历过
            if reach[box_x][box_y][player_x][player_y] < 0:
                queue.append([box_x, box_y, player_x, player_y])
                reach[box_x][box_y][player_x][player_y] = reach[cur[0]][cur[1]][cur[2]][cur[3]] + 1

if cur[0] != end[0] or cur[1] != end[1]:
    print(-1)