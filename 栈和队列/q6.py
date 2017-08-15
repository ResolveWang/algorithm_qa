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
2）使用栈来模拟汉诺塔的三个塔

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

if __name__ == '__main__':
    n1 = 2
    n2 = 4

    steps = RecursiveWay.move(n1, RecursiveWay.left, RecursiveWay.mid, RecursiveWay.right)
    print('total steps is {}'.format(steps))
    print('*********************************')
    steps = RecursiveWay.move(n2, RecursiveWay.left, RecursiveWay.mid, RecursiveWay.right)
    print('total steps is {}'.format(steps))