"""
问题描述：给定一个整数n,代表汉诺塔游戏中从小到大放置的n个圆盘，假设开始时所有的圆盘都
放在左边的柱子上，想按汉诺塔游戏的要求把所有的圆盘都移动到右边的柱子上，实现函数打印最
优移动轨迹。
例如：
n=1时，打印：
move from left to right
n=2时，打印:
move from left to mid
move from left to right
move from mid to right
"""


class Hanoi:
    @classmethod
    def main(cls, n):
        if n == 0:
            return
        cls.move(n, 'left', 'mid', 'right')

    @classmethod
    def move(cls, n, move_from, move_mid, move_to):
        if n == 1:
            print('move from {} to {}'.format(move_from, move_to))
        else:
            cls.move(n-1, move_from, move_to, move_mid)
            cls.move(1, move_from, move_mid, move_to)
            cls.move(n-1, move_mid, move_from, move_to)


if __name__ == '__main__':
    Hanoi.main(2)