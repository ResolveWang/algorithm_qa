"""
问题描述:有序数组arr可能经过一次旋转处理,也可能没有,且arr可能存在重复
的数.例如,有序数组[1,2,3,4,5,6,7],可以旋转成[4,5,6,7,1,2,3]等。给
定一个可能旋转过的有序数组arr,再给定一个数num,返回arr中是否含有num.
"""


class NumberFinder:
    @classmethod
    def is_exists(cls, arr, num):
        if not arr:
            return False

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = int(int(high - low) / 2 + low)
            if arr[mid] == num:
                return True
            if arr[low] == arr[mid] == arr[high]:
                while arr[low] == arr[mid] and low != mid:
                    low += 1
                    if low == mid:
                        low += 1

            if low == mid:
                low += 1
                continue

            if arr[low] < arr[mid]:
                if arr[low] <= num < arr[mid]:
                    high -= 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < num <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


if __name__ == '__main__':
    print(NumberFinder.is_exists([4, 5, 6, 7, 1, 2, 3], 3))
    print(NumberFinder.is_exists([4, 5, 6, 7, 1, 2, 3], 9))