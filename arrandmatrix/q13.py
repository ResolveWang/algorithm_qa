"""
数组小和定义如下:
例如,数组s=[1,3,5,2,4,6],在s[0]的左边小于或者等于s[0]的数的和为0,在s[1]的
左边小于或者等于s[1]的数的和为１,在s[2]的左边小于或者等于s[2]的数的和为1+3=4,
在s[3]的左边小于等于s[3]的数的和为1,在s[4]的左边小于或者等于s[4]的数的和为1+3+2=6,
在s[5]的左边小于或等于s[5]的数的和为1+3+5+2+4=15,所以s的小和为0+1+4+1+6+15=27.
给定一个数组s,实现函数返回s的小和。
"""


class SmallSum:
    small_sum = 0

    @classmethod
    def get_small_sum(cls, arr):
        if not arr:
            return 0

        cls.merge_sort(arr, 0, len(arr)-1)
        return cls.small_sum

    @classmethod
    def merge_sort(cls, arr, index, end):
        if index == end:
            return

        mid = int((index + end)/2)

        cls.merge_sort(arr, index, mid)
        cls.merge_sort(arr, mid+1, end)
        cls.merge(arr, index, mid, end)

    @classmethod
    def wrong_merge(cls, arr, arr_left, arr_mid, arr_right):
        left_index = arr_left
        right_index = arr_mid + 1
        while left_index <= arr_mid and right_index <= arr_right:
            if arr[left_index] <= arr[right_index]:
                cls.small_sum += (arr_right - right_index + 1) * arr[left_index]
                left_index += 1
            else:
                arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
                tmp_index = right_index
                while tmp_index < arr_right and arr[tmp_index] > arr[tmp_index+1]:
                    arr[tmp_index], arr[tmp_index+1] = arr[tmp_index+1], arr[tmp_index]
                    tmp_index += 1
                left_index += 1

    @classmethod
    def merge(cls, arr, arr_left, arr_mid, arr_right):
        """这里不能用就地交换,需要使用辅助数组，因为循环内每个比较需要数据原来的位置"""
        help_arr = [0 for _ in range(arr_right-arr_left+1)]

        i = 0
        left_index = arr_left
        right_index = arr_mid + 1

        while left_index <= arr_mid and right_index <= arr_right:
            if arr[left_index] <= arr[right_index]:
                cls.small_sum += arr[left_index] * (arr_right - right_index + 1)
                help_arr[i] = arr[left_index]
                left_index += 1
            else:
                help_arr[i] = arr[right_index]
                right_index += 1
            i += 1

        while left_index <= arr_mid:
            help_arr[i] = arr[left_index]
            left_index += 1
            i += 1

        while right_index <= arr_right:
            help_arr[i] = arr[right_index]
            right_index += 1
            i += 1

        for i in range(len(help_arr)):
            arr[arr_left+i] = help_arr[i]


if __name__ == '__main__':
    my_arr = [1, 3, 5, 2, 4, 6]
    print(SmallSum.get_small_sum(my_arr))