"""
随机快速排序
"""

import random

from basic_algrithms.sort_algrithms.benchmark import Comparator


def partition(arr, l, r):
    less = l - 1
    more = r
    while l < more:
        if arr[l] < arr[r]:
            less += 1
            arr[less], arr[l] = arr[l], arr[less]
            l += 1
        elif arr[l] > arr[r]:
            more -= 1
            arr[l], arr[more] = arr[more], arr[l]
        else:
            l += 1

    arr[more], arr[r] = arr[r], arr[more]
    return less, more


def random_quick_sort_detail(arr, l, r):
    if l < r:
        random_index = l + int(random.random() * (r - l + 1))
        arr[random_index], arr[r] = arr[r], arr[random_index]
        pos = partition(arr, l, r)
        random_quick_sort_detail(arr, l, pos[0])
        random_quick_sort_detail(arr, pos[1]+1, r)


def random_quick_sort(arr):
    if not arr or len(arr) < 2:
        return arr

    random_quick_sort_detail(arr, 0, len(arr)-1)
    return arr


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        sorted_arr1 = random_quick_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(sorted_arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')
