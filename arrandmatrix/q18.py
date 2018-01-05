"""
问题描述:定义局部最小的概念。arr长度为1时,arr[0]是局部最小。arr长度为N(N>1)时，
如果arr[0]<arr[1],那么arr[0]是局部最小;如果arr[N-1]<arr[N-2],那么arr[N-1]
是局部最小;如果0<i<N-1,既有arr[i]<arr[i-1],又有arr[i]<arr[i+1],那么arr[i]
是局部最小。
给定一个无序数组arr,已知arr中任意两个相邻的数都不相等。写一个函数,只需返回arr中任意
一个局部最小出现的位置即可。
"""


class LocalMinValue:
    @classmethod
    def get_local_min_value(cls, arr):
        if not arr:
            return

        if len(arr) == 1:
            return 0

        if arr[0] < arr[1]:
            return 0

        if arr[-1] < arr[-2]:
            return len(arr) - 1

        return cls.get_local_min_value_detail(arr, 0, len(arr)-1)

    @classmethod
    def get_local_min_value_detail(cls, arr, start, end):
        if start == end:
            return start

        mid = start + ((end - start) >> 1)
        if arr[mid-1] < arr[mid]:
            return cls.get_local_min_value_detail(arr, start, mid-1)
        if arr[mid+1] < arr[mid]:
            return cls.get_local_min_value_detail(arr, mid+1, end)

        return mid


if __name__ == '__main__':
    my_arr = [6, 5, 3, 4, 6, 7, 8]
    print(LocalMinValue.get_local_min_value(my_arr))