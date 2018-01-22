"""
问题描述:有序数组arr可能经过一次旋转,也可能没有,且arr可能存在重复的数,
例如，有序数组[1,2,3,4,5,6,7],可以旋转处理成[4,5,6,7,1,2,3]等。给定
一个可能旋转过的有序数组,返回arr的最小值.

变型：找出旋转数组的中位数
思路还是找到最小值（断点）,由于找到最小值后，我们可以很方便的找到离最小值m
个位置的数
"""


class SmallnestNumFinder:
    @classmethod
    def get_smallest_num(cls, arr):
        if not arr:
            return

        if len(arr) == 1:
            return arr[0]

        low = 0
        high = len(arr) - 1

        while True:
            if arr[low] < arr[high]:
                return arr[low]
            mid = int((high - low)/2) + low
            if mid == low:
                return arr[high]

            if arr[mid] > arr[high]:
                # deal mid to high
                low = mid
            elif arr[mid] < arr[low]:
                # deal low to mid
                high = mid
            else:
                cur = low
                while arr[cur] == arr[high]:
                    cur += 1
                if arr[cur] < arr[high]:
                    return arr[cur]
                else:
                    low = cur


if __name__ == '__main__':
    print(SmallnestNumFinder.get_smallest_num([4, 5, 5, 5, 1, 2, 3]))
