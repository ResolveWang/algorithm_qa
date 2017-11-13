"""
选择排序
"""

from basic_algrithms.sort_algrithms.benchmark import Comparator


def select_sort(arr):
    if not arr or len(arr) < 2:
        return arr

    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        sorted_arr1 = select_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(sorted_arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')