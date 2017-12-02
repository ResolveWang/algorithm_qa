"""
问题描述：给定一个数组arr,arr[i]=k代表可以从位置i向右跳1~k个距离。比如，arr[2]==3,
代表可以从位置2跳到位置3、位置4或者位置5.如果从位置0出发，返回最少跳几次能跳到arr最后的
位置上。

举例:
arr=[3,2,3,1,1,4]
arr[0]=3,选择跳到位置2；arr[2]=3,可以跳到最后的位置，所以返回2。

要求：
如果arr长度为N，要求实现时间复杂度为O(N)、额外空间复杂度为O(1)的方法。
"""


class JumpSteps:
    @classmethod
    def get_steps(cls, arr):
        if not arr:
            return 0

        jump = 0
        cur_pos = 0
        next_pos = 0

        for i in arr:
            if cur_pos < i:
                jump += 1
                cur_pos = next_pos

            next_pos = max([arr[i]+i, next_pos])

        return jump


if __name__ == '__main__':
    print(JumpSteps.get_steps([3, 2, 3, 1, 1, 4]))