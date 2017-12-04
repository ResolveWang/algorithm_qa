"""
shell排序
"""


from basic_algrithms.sort_algrithms.benchmark import Comparator


class ShellSort:
    @classmethod
    def shell_sort(cls, arr):
        if len(arr) < 1:
            return arr

        arr_len = len(arr)
        gap = arr_len // 2
        while gap > 0:
            for i in range(gap, arr_len):
                temp = arr[i]
                while i >= gap and arr[i-gap] > temp:
                    arr[i] = arr[i-gap]
                    i -= gap
                arr[i] = temp
            gap = gap//2
        return arr


if __name__ == '__main__':
    max_times = 1000
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        sorted_arr1 = ShellSort.shell_sort(arr1)
        sorted_arr2 = sorted(arr2)
        if not Comparator.is_equal(sorted_arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')