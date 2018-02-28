"""
问题描述:给定两个有序数组arr1和arr2，再给定一个整数k，返回所有的数中
第k小的数。
举例:
arr1=[1, 2, 3, 4, 5],arr2=[3, 4, 5], k=1, 返回１
arr1=[1, 2, 3], arr2=[3, 4, 5, 6], k=4，返回3

要求:
如果arr1的长度为N,arr2的长度为M,时间复杂度请达到O(log(min{M,N})),额外
空间复杂度为O(1)
"""
from other.q26 import MiddleNumFinder


class KthNumFinder:
    @classmethod
    def get_kth_num(cls, arr1, arr2, k):
        if k < 1 or k > len(arr1) + len(arr2):
            return

        short_arr = arr1 if len(arr1) <= len(arr2) else arr2
        long_arr = arr1 if len(arr1) > len(arr2) else arr2
        slen = len(short_arr)
        llen = len(long_arr)

        if k <= slen:
            return MiddleNumFinder.find_pre_middle_num(arr1[:k], arr2[:k])
        elif k > llen:
            if short_arr[-1] <= long_arr[0]:
                return long_arr[k-slen-1]
            if long_arr[-1] <= short_arr[0]:
                return short_arr[k-llen-1]
            return MiddleNumFinder.find_pre_middle_num(short_arr[k-llen:], long_arr[k-slen:])
        else:
            return MiddleNumFinder.find_pre_middle_num(short_arr, long_arr[k-slen:k])


if __name__ == '__main__':
    print(KthNumFinder.get_kth_num([1, 2, 3, 4, 5], [3, 4, 5], 1))
    print(KthNumFinder.get_kth_num([1, 2, 6], [3, 4, 7, 21], 5))
    print(KthNumFinder.get_kth_num([1, 2, 6, 9, 23, 14], [3, 4, 7, 21], 5))