"""
问题描述:给定两个有序数组arr1和arr2,已知两个数组的长度都为N，求两个数组
中所有数的上中位数。

举例:
arr1=[1, 2, 3, 4], arr2=[3, 4, 5, 6]
总共有8个数，那么上中位数是第4小的数，所以返回3
arr1=[0, 1, 2], arr2=[3, 4, 5]
总共有6个数，那么上中位数是第3小的数，所以返回2

要求:
时间复杂度为O(logN),额外空间复杂度为O(1)
"""


class MiddleNumFinder:
    @classmethod
    def find_pre_middle_num(cls, arr1, arr2):
        if not arr1 or not arr2 or len(arr1) != len(arr2):
            return

        length = len(arr1)
        start1 = 0
        start2 = 0
        end1 = length - 1
        end2 = length - 1

        while start1 < end1:
            mid1 = (start1 + end1) >> 1
            mid2 = (start2 + end2) >> 1
            if arr1[mid1] == arr2[mid2]:
                return arr1[mid1]
            elif arr1[mid1] > arr2[mid2]:
                if (end1 - start1 + 1) % 2 == 1:
                    end1 = mid1
                    start2 = mid2
                else:
                    end1 = mid1
                    start2 = mid2 + 1
            else:
                if (end1 - start1 + 1) % 2 == 1:
                    end2 = mid2
                    start1 = mid1
                else:
                    end2 = mid2
                    start1 = mid1 + 1
        return min([arr1[start1], arr2[start2]])


if __name__ == '__main__':
    print(MiddleNumFinder.find_pre_middle_num([1, 2, 3, 4], [3, 4, 5, 6]))
    print(MiddleNumFinder.find_pre_middle_num([1, 2, 3, 4], [5, 6, 7, 8]))
    print(MiddleNumFinder.find_pre_middle_num([1, 2, 3, 4], [5, 6, 7, 8]))
    print(MiddleNumFinder.find_pre_middle_num([2, 7, 10, 10, 14, 14, 20],
                                              [4, 13, 13, 13, 21, 33, 47]))