"""
冒泡排序，注意这里会修改数组元素的位置顺序
"""


from basic_algrithms.sort_algrithms.benchmark import Comparator


def bubble_sort(arr):
    if not arr or len(arr) < 2:
        return arr

    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            # 只大于不等于可以保证稳定性
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':
    max_times = 500
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        bubble_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')