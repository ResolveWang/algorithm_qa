"""
给定一个字符串类型的数组strs，请找到一种拼接顺序，使得将所有的字符串拼接起来组成的大写
字符串是所有可能性中字典顺序最小的，并返回这个大写字符串。

举例：
strs=['abc', 'de']，可以拼成'abcde'，也可以拼接成'deabc'，但前者的字典顺序更小，所
以返回'abcde'.
strs=['b', 'ba']，可以拼接成'bba'，也可以拼接成'bab'，但后者的字典顺序更小，所以返回
'bab'.
"""


class StrComparator:
    @classmethod
    def get_max_str(cls, arr):
        if not arr:
            return ''
        cls.merge_sort(arr)
        return ''.join(arr)

    @classmethod
    def merge_sort(cls, arr):
        if len(arr) < 2:
            return arr

        cls.merge_sort_detail(arr, 0, len(arr)-1)

    @classmethod
    def merge_sort_detail(cls, arr, l, r):
        if l == r:
            return

        mid = l + ((r-l) >> 1)
        cls.merge_sort_detail(arr, l, mid)
        cls.merge_sort_detail(arr, mid+1, r)
        cls.merge(arr, l, mid, r)

    @classmethod
    def merge(cls, arr, l, m, r):
        help_arr = ['' for _ in range(r-l+1)]
        base_str = '{}{}'
        i = 0
        p1 = l
        p2 = m + 1

        while p1 <= m and p2 <= r:
            if base_str.format(arr[p1], arr[p2]) < base_str.format(arr[p2], arr[p1]):
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
    arr1 = ["jibw", "ji", "jp", "bw", "jibw"]
    print(StrComparator.get_max_str(arr1))

    arr2 = ["ba", "b"]
    print(StrComparator.get_max_str(arr2))

