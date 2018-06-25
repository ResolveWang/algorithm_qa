"""
问题描述: 牛牛与妞妞闲来无聊，便拿出扑克牌来进行游戏。游戏的规则很简单，两个人随机
抽取四张牌，四张牌的数字和最大的取胜（该扑克牌总张数为52张，没有大小王，A=1，J=11，
Q=12，K=13，每种数字有四张牌），现在两人已经分别亮出了自己的前三张牌，牛牛想要知
道自己要赢得游戏的概率有多大。

输入包含两行，第一行输入三个整数a1，b1，c1(1≤a1，b1，c1≤13)，表示牛牛亮出的扑克牌。
第二行输入三个整数a2，b2，c2(1≤a2，b2，c2≤13)，表示妞妞所亮出的扑克牌。

示例:
3 5 7
2 6 8

输出:
0.3995
"""


class Solution:
    def get_properties(self, a1, a2, a3, b1, b2, b3):
        a = [0 for _ in range(60)]
        vis = [0 for _ in range(15)]
        vis[a1] += 1
        vis[a2] += 1
        vis[a3] += 1
        vis[b1] += 1
        vis[b2] += 1
        vis[b3] += 1
        sum1 = a1 + a2 + a3
        sum2 = b1 + b2 + b3
        cnt = 0
        l, r = 0, 0
        for i in range(1, 14):
            for j in range(0, 4-vis[i]):
                a[cnt] = i
                cnt += 1

        for i in range(cnt):
            sum1 += a[i]
            for j in range(cnt):
                if i == j:
                    continue
                sum2 += a[j]
                r += 1
                if sum1 > sum2:
                    l += 1
                sum2 -= a[j]
            sum1 -= a[i]
        print('%.4f' % (l / r))


if __name__ == '__main__':
    s = Solution()
    a, b, c = list(map(int, input().split()))
    d, e, f = list(map(int, input().split()))
    s.get_properties(a, b, c, d, e, f)