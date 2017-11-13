"""
二分搜索
"""


from basic_algrithms.search_algrithms.benchmark import Comparator


def binary_search(arr, value):
    if not arr:
        return False
    length = len(arr)
    left = 0
    right = length-1

    while left <= right:
        mid = left + ((right-left) >> 1)
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1

    return False


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for i in range(max_times):
        arr = Comparator.gen_random_array(max_size, max_value)
        value = Comparator.gen_random_value(max_value)

        res1 = binary_search(arr, value)
        res2 = Comparator.compare_with_bench(arr, value)

        if res1 != res2:
            print(arr)
            print(value)
            print(res1)
            print(res2)
            res = False
            break

    if res:
        print('Success')
    else:
        print('Failed')

