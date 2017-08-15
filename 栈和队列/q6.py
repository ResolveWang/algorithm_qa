"""
问题描述：汉诺塔问题比较经典，现在修改一下规则：现在限制不能从最左侧的塔直接移动到最右侧，
也不能从最右侧直接移动到最左侧，而必须经过中间，求当塔有N层的时候，打印最优移动过程和最优
移动总步数。比如N=2，则打印：
move 1 from left to mid
move 1 from mid to right
move 2 from left to mid
move 1 from right to mid
move 1 from mid to left
move 2 from mid to right
move 1 from left to mid
move 1 from mid to right
it will move 8 steps

要求：
1）使用递归的方案
2）非递归的方法，使用栈来模拟汉诺塔的三个塔

思路：
a)将1~(N-1)层塔先全部从左移动到右，递归过程
b)将第N层塔从左移动到中
c)将1~(N-1)层塔全部从右移动到左，递归过程
d)将第N层塔从中移动到右
e)将1~(N-1)层塔全部从左移动到右，递归
"""


class RecursiveWay:
    left = 'left'
    mid = 'mid'
    right = 'right'

    @classmethod
    def move(cls, n, left, mid, right):
        if n == 0:
            return 0

        if n == 1:
            print('move {} from {} to {}'.format(n, left, mid))
            print('move {} from {} to {}'.format(n, mid, right))
            return 2
        else:
            total = RecursiveWay.move(n-1, left, mid, right)

            print('move {} from {} to {}'.format(n, left, mid))
            total += 1

            total += RecursiveWay.move(n-1, right, mid, left)

            print('move {} from {} to {}'.format(n, mid, right))
            total += 1

            total += RecursiveWay.move(n - 1, left, mid, right)

            return total


import sys

class MoveDetail:
    MoveNone = 0
    L2M = 1
    M2L = 3
    M2R = 2
    R2M = 4


class StackHannota:
    left = list()
    mid = list()
    right = list()

    left.append(sys.maxsize)
    mid.append(sys.maxsize)
    right.append(sys.maxsize)

    left_side = 'left'
    mid_side = 'mid'
    right_side = 'right'

    steps = 0

    lastmove = MoveDetail.MoveNone

    @classmethod
    def move(cls):
        n = len(cls.left)-1
        if n == 0:
            return 0
        if n == 1:
            print('move {} from {} to {}'.format(n, 'left', 'mid'))
            print('move {} from {} to {}'.format(n, 'mid', 'right'))
            return 2
        while len(cls.left) > 1 or len(cls.mid) > 1:
            cls.process(cls.lastmove, MoveDetail.L2M, cls.left_side, cls.mid_side, cls.left, cls.mid)
            cls.process(cls.lastmove, MoveDetail.M2L, cls.mid_side, cls.left_side, cls.mid, cls.left)
            cls.process(cls.lastmove, MoveDetail.M2R, cls.mid_side, cls.right_side, cls.mid, cls.right)
            cls.process(cls.lastmove, MoveDetail.R2M, cls.right_side, cls.mid_side, cls.right, cls.mid)

    @classmethod
    def process(cls, lastmove, curmove, efrom, eto, fstack, tstack):
        if fstack[-1] < tstack[-1] and abs(lastmove-curmove) != 2:
            i = fstack.pop()
            print('move {} from {} to {}'.format(i, efrom, eto))
            tstack.append(i)
            cls.steps += 1
            cls.lastmove = curmove
        return


if __name__ == '__main__':
    n1 = 2
    n2 = 4

    steps = RecursiveWay.move(n1, RecursiveWay.left, RecursiveWay.mid, RecursiveWay.right)
    print('total steps is {}'.format(steps))
    print('*********************************')
    for i in reversed(range(1, n2+1)):
        StackHannota.left.append(i)
    StackHannota.move()
    print('total steps is {}'.format(StackHannota.steps))