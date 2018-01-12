"""
问题描述:请把一段纸条竖着放在桌子上,然后从纸条的下边向上方对折１次,压出折痕后
展开,此时折痕是凹下去的,即折痕凸起的方向指向纸条的背面.如果从纸条的下边向上方
连续对折2次,压出折痕后展开,此时有三条折痕,从上到下依次是下折痕、下折痕和上折痕.
给定一个输入参数N,代表纸条都从下边向上方连续对折N次,请从上到下打印所有折痕的
方向。

例如:
N=1时,打印:
down
N=2时,打印:
down
down
up
"""


class FoldProblem:
    @classmethod
    def get_folds(cls, n):
        cls.deal_with_detail(1, n, True)

    @classmethod
    def deal_with_detail(cls, i, n, is_down):
        if i > n:
            return

        cls.deal_with_detail(i+1, n, True)
        if is_down:
            print('down')
        else:
            print('up')
        cls.deal_with_detail(i+1, n, False)


if __name__ == '__main__':
    FoldProblem.get_folds(3)