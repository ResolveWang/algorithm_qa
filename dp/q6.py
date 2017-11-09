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

进阶：给定一个整型数组arr,其中只含有1、2和3，代表所有圆盘目前的状态，1代表左柱，2代表中柱，
3代表右柱，arr[i]的值代表第i+1个圆盘的位置。比如,arr=[3, 3, 2, 2]，代表第一个圆盘在右
柱上，第二个圆盘在右柱上，第三个圆盘在中柱上，第四个圆盘在左柱上。如果arr代表的状态是最优移
动轨迹过程中出现的状态，返回arr这种状态是最优移动轨迹中的第几个状态。如果arr代表的状态不是最
优移动轨迹中出现的状态，则返回-1。

举例：
arr=[1, 1]。两个圆盘目前都在左柱上，也就是初始状态，返回0.
arr=[2, 1]。第一个圆盘在中柱上，第二个在左柱上，这个状态是2个圆盘的汉诺塔游戏中最优移动轨迹的
第一步，所以返回1.
arr=[3, 3]。第一个圆盘在右柱上，第二个圆盘在右柱上，这个状态是2个圆盘的汉诺塔游戏中最优移动轨
迹的第三布，所以返回3.
arr=[2, 2]。第一个圆盘在中柱上，第二个圆盘在中柱上，这个状态是2个圆盘的汉诺塔游戏中最优移动轨迹
从来不会出现的状态，所以返回-1。

要求：如果arr长度为N，请实现时间复杂度为O(N)、额外空间复杂度为O(1)的方法。
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

    @classmethod
    def step_1(cls, arr):
        if not arr:
            return -1

        return cls.detail_1(arr, len(arr)-1, 1, 2, 3)

    @classmethod
    def detail_1(cls, arr, index, move_from, move_mid, move_to):
        if index == -1:
            return 0

        # 末尾的盘子不可能移动在中间
        if arr[index] == move_mid:
            return -1
        # 盘子并未移动或者移动完成
        if arr[index] == move_from:
            return cls.detail_1(arr, index-1, move_from, move_to, move_mid)
        else:
            res = cls.detail_1(arr, index-1, move_mid, move_from, move_to)
            if res == -1:
                return -1

            return (1 << index) + res

    @classmethod
    def step_2(cls, arr):
        if not arr:
            return -1

        move_from = 1
        move_mid = 2
        move_to = 3
        res = 0

        index = len(arr) - 1
        while index >= 0:
            if arr[index] == move_mid:
                return -1

            if arr[index] == move_from:
                temp = move_mid
                move_mid = move_to
                move_to = temp
            else:
                temp = move_from
                move_from = move_mid
                move_mid = temp

                res += (1 << index)

            index -= 1
        return res


if __name__ == '__main__':
    Hanoi.main(2)
    my_arr = [3, 3, 2, 1]
    print(Hanoi.step_2(my_arr))
    print(Hanoi.step_1(my_arr))