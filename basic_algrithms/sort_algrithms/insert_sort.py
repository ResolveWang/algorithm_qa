"""
插入排序
"""


from basic_algrithms.sort_algrithms.benchmark import Comparator


def insert_sort(arr):
    if not arr or len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        sorted_arr1 = insert_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(sorted_arr1, sorted_arr2):
            res = False
            break
    if not res:
        print('Failed ')
    else:
        print('Success')
