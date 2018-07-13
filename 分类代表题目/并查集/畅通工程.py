"""
问题描述: 某省调查城镇交通状况，得到现有城镇道路统计表，表中列出了每条道路直接连通的城镇。
省政府“畅通工程”的目标是使全省任何两个城镇间都可以实现交通（但不一定有直接的道路相连，只
要互相间接通过道路可达即可）。问最少还需要建设多少条道路？

输入描述:
测试输入包含若干测试用例。每个测试用例的第1行给出两个正整数，分别是城镇数目N ( < 1000 )和
道路数目M；随后的M行对应M条道路，每行给出一对正整数，分别是该条道路直接连通的两个城镇的编号。
为简单起见，城镇从1到N编号。
注意:两个城市之间可以有多条道路相通,也就是说
3 3
1 2
1 2
2 1
这种输入也是合法的
当N为0时，输入结束，该用例不被处理。

输出描述: 对每个测试用例，在1行里输出最少还需要建设的道路数目。

示例1
输入
4 2
1 3
4 3

3 3
1 2
1 3

2 3
5 2
1 2

3 5
999 0
0

输出
1
0
2
998
"""
import sys


class Solution:
    """并查集的应用"""

    def find(self, pre, index):
        """pre每个位置的下标对应节点值，而pre[index]对应节点值的前一个数"""
        if pre[index] == index:
            return index
        else:
            tmp = self.find(pre, pre[index])
            pre[index] = tmp
            return tmp

    def union(self, u, v, pre):
        node1 = self.find(pre, u)
        node2 = self.find(pre, v)
        if node1 != node2:
            pre[node2] = node1

    def get_roads(self):
        n, m = map(int, sys.stdin.readline().split())
        count = 0
        pre = [i for i in range(n+1)]
        for i in range(m):
            x, y = [int(x) for x in sys.stdin.readline().split()]
            self.union(x, y, pre)

        for i in range(1, n+1):
            if pre[i] == i:
                count += 1

        print(count-1)


if __name__ == '__main__':
    s = Solution()
    s.get_roads()
