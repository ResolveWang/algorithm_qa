"""
问题描述: 小易总是感觉饥饿，所以作为章鱼的小易经常出去寻找贝壳吃。最开始小易在一个初始位置x_0。
对于小易所处的当前位置x，他只能通过神秘的力量移动到 4 * x + 3或者8 * x + 7。因为使用神秘力
量要耗费太多体力，所以它只能使用神秘力量最多100,000次。贝壳总生长在能被1,000,000,007整除的
位置(比如：位置0，位置1,000,000,007，位置2,000,000,014等)。小易需要你帮忙计算最少需要使
用多少次神秘力量就能吃到贝壳。

输入描述:
输入一个初始位置x_0,范围在1到1,000,000,006
输出描述:
输出小易最少需要使用神秘力量的次数，如果使用次数使用完还没找到贝壳，则输出-1
示例1
输入
125000000
输出
1
"""

import sys


class Solution:
    def get_res(self, pos):
        queue = [pos]
        visited = {pos: 0}
        find_food = False
        while len(queue):
            cur_pos = queue.pop(0)

            if cur_pos == 0:
                find_food = True
                break
            if visited.get(cur_pos, 0) > 100000:
                break
            else:
                next_pos = (4 * cur_pos + 3) % 1000000007
                if next_pos not in visited:
                    queue.append(next_pos)
                    visited[next_pos] = visited[cur_pos] + 1

                next_pos = (8 * cur_pos + 7) % 1000000007
                if next_pos not in visited:
                    queue.append(next_pos)
                    visited[next_pos] = visited[cur_pos] + 1
        if find_food:
            print(visited[cur_pos])
        else:
            print(-1)


if __name__ == '__main__':
    args = int(sys.stdin.readline().strip())
    solution = Solution()
    solution.get_res(args)
