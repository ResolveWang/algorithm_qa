"""
归并排序
"""


from basic_algrithms.sort_algrithms.benchmark import Comparator


class MergeSort:
    @classmethod
    def merge_sort(cls, arr):
        if not arr or len(arr) < 2:
            return arr
        cls.merge_sort_detail(arr, 0, len(arr)-1)

    @classmethod
    def merge_sort_detail(cls, arr, l, r):
        if r == l:
            return

        mid = l + ((r-l) >> 1)
        cls.merge_sort_detail(arr, l, mid)
        cls.merge_sort_detail(arr, mid+1, r)
        cls.merge(arr, l, mid, r)

    @classmethod
    def merge(cls, arr, l, m, r):
        help_arr = [0 for _ in range(r-l+1)]

        i = 0
        p1 = l
        p2 = m + 1

        while p1 <= m and p2 <= r:
            if arr[p1] < arr[p2]:
                help_arr[i] = arr[p1]
                p1 += 1
            else:
                help_arr[i] = arr[p2]
                p2 += 1
            i += 1

        while p1 <= m:
            help_arr[i] = arr[p1]
            p1 += 1
            i += 1

        while p2 <= r:
            help_arr[i] = arr[p2]
            p2 += 1
            i += 1

        for i in range(len(help_arr)):
            arr[l+i] = help_arr[i]


if __name__ == '__main__':
    max_times = 5000
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)

        MergeSort.merge_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')