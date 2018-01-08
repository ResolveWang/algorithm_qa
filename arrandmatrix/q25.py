"""
问题描述:给定一个无序整型数组arr,找到数组中未出现的最小正整数.

举例:
arr=[-1, 2, 3, 4],返回1
arr=[1, 2, 3, 4],返回５
"""


class SmallestNumFinder:
    @classmethod
    def get_the_smallest_num(cls, arr):
        if not arr:
            return 1

        l = 0
        r = len(arr)

        while l < r:
            if arr[l] == l + 1:
                l += 1
                print('l', l)
            elif arr[l] <= l or arr[l] > r or arr[arr[l]-1] == arr[l]:
                r -= 1
                arr[l] = arr[r]
            else:
                cls.swap(arr, l, arr[l]-1)

        return l + 1

    @classmethod
    def swap(cls, arr, index1, index2):
        tmp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = tmp


if __name__ == '__main__':
    my_arr = [-1, 1, 2, 3, 4]
    print(SmallestNumFinder.get_the_smallest_num(my_arr))