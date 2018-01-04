"""
问题描述:给定一个长度不小于２的数组arr,实现一个函数调整arr,要么让所有的偶数
下标都是偶数,要么让所有的奇数下标都是奇数.

要求:
如果arr的长度为N,函数要求时间复杂度为O(N),额外空间复杂度为O(1).
"""


class EvenOddPlacer:
    @classmethod
    def place_the_num(cls, arr):
        even_num = 0
        odd_num = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                odd_num += 1
            else:
                even_num += 1

        # 数量小的必然有足够的位置放置, j只进不退，则时间复杂度为O(N)
        if odd_num <= even_num:
            i = 0
            j = 1
            while i < len(arr):
                while arr[i] % 2 != 0 and j < len(arr):
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 2
                i += 2
        else:
            i = 1
            j = 0
            while i < len(arr):
                while arr[i] % 2 == 0 and j < len(arr):
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 2
                i += 2

        return arr


if __name__ == '__main__':
    my_arr = [1, 8, 3, 2, 4, 6]
    print(EvenOddPlacer.place_the_num(my_arr))