"""
桶排序
"""


import sys

from basic_algrithms.sort_algrithms.benchmark import Comparator


class BucketSort:
    @classmethod
    def bucket_sort(cls, arr):
        if not arr or len(arr) < 2:
            return arr
        # 系统最小值
        max_value = -sys.maxsize
        # max(arr) 找到数组最大值
        for i in arr:
            max_value = i if i > max_value else max_value
        # 由待排序的最大值确定桶的大小
        bucket = [0 for _ in range(max_value+1)]
        # 对值进行计数
        for i in arr:
            bucket[i] += 1

        start = 0
        for index, value in enumerate(bucket):
            if value == 0:
                continue
            else:
                # 重新组织arr
                while value > 0:
                    arr[start] = index
                    value -= 1
                    start += 1

        return arr


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)
        sorted_arr1 = BucketSort.bucket_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(sorted_arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')
