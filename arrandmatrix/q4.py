"""
问题描述:给定一个无序的整型数组arr,找到其中最小的k个数。
要求:
如果数组arr的长度为N,排序之后自然可以得到最小的k个数，此时时间复杂度与排序时间
复杂度相同，为O(NlogN)，本地要求读者实现时间复杂度为O(NlogK)和O(logN)的解法。
"""
from basic_algrithms.search_algrithms.bfprt import BFPRT


class HeapSortSolver:
    """维持一个size为k的大根堆即可"""
    @classmethod
    def get_k_small_nums(cls, arr, k):
        if not k or len(arr) <= k:
            return arr

        for i in range(k):
            cls.heap_insert(arr, i)

        for i in range(k, len(arr)):
            if arr[0] > arr[i]:
                arr[0], arr[i] = arr[i], arr[0]
                cls.heapify(arr, 0, k)

        return arr[:k]

    @classmethod
    def heap_insert(cls, arr, index):
        while arr[index] > arr[int((index-1)/2)]:
            arr[index], arr[int((index-1)/2)] = arr[int((index-1)/2)], arr[index]
            index = int((index-1)/2)

    @classmethod
    def heapify(cls, arr, index, size):
        left = index * 2 + 1
        while left < size:
            if left + 1 < size and arr[left+1] > arr[left]:
                largest = left + 1
            else:
                largest = left

            if arr[index] >= arr[largest]:
                return

            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
            left = index * 2 + 1


class BFPRTSolver(BFPRT):
    @classmethod
    def get_k_small_nums(cls, arr, k):
        if not k or len(arr) <= k:
            return arr

        kth_num = cls.get_the_k_number(arr, k)
        res = [kth_num]
        for i in arr:
            if i < kth_num:
                res.append(i)
        diff = k - len(res)
        for _ in range(diff):
            res.append(kth_num)

        return res


if __name__ == '__main__':
    my_arr = [6, 9, 1, 3, 1, 2, 2, 5, 6, 1, 3, 5, 9, 7, 2, 5, 6, 1, 9]
    print(HeapSortSolver.get_k_small_nums(my_arr, 10))
    print(BFPRTSolver.get_k_small_nums(my_arr, 10))