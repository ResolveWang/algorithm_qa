"""
问题描述: 一闪一闪亮晶晶，满天都是小星星，牛牛晚上闲来无聊，便躺在床上数星星。牛牛把星星图看成一个
平面，左上角为原点(坐标为(1, 1))。现在有n颗星星，他给每颗星星都标上坐标(xi，yi)，表示这颗星星
在第x行，第y列。现在，牛牛想问你m个问题，给你两个点的坐标(a1, b1)(a2，b2)，表示一个矩形的左上
角的点坐标和右下角的点坐标，请问在这个矩形内有多少颗星星（边界上的点也算是矩形内）。

举例
输入:
4
1 1
2 2
3 3
1 3
4
1 1 2 2
1 1 3 3
2 2 3 3
1 2 2 3

输出:
2
4
2
2
"""


import sys


class StarCounter:
    def get_num(self):
        n = int(sys.stdin.readline().strip())
        data = [[0 for _ in range(1001)] for _ in range(1001)]
        for i in range(n):
            line = sys.stdin.readline().strip()
            p0, p1 = list(map(int, line.split()))
            data[p0][p1] = 1
        for i in range(1, 1001):
            for j in range(1, 1001):
                data[i][j] += data[i][j-1] + data[i-1][j] - data[i-1][j-1]

        m = int(sys.stdin.readline().strip())
        for i in range(m):
            line = sys.stdin.readline().strip()
            a1, b1, a2, b2 = list(map(int, line.split()))
            rs = data[a2][b2]-data[a2][b1-1]-data[a1-1][b2]+data[a1-1][b1-1]
            print(rs)
            del a1, b1, a2, b2, line


if __name__ == '__main__':
    star_counter = StarCounter()
    star_counter.get_num()