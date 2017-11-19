"""
堆排序.
（1）堆排序的常数项比较大，适用于大型数组排序。
（2）时间复杂度是O(Nlog(N)),空间复杂度是O(1)。
（3）堆排序是不稳定的排序。
"""


from basic_algrithms.sort_algrithms.benchmark import Comparator


class HeapSort:
    @classmethod
    def heap_sort(cls, arr):
        if not arr or len(arr) < 2:
            return arr

        cls.heap_sort_detail(arr)

    @classmethod
    def heap_sort_detail(cls, arr):
        # 建立大顶堆，这里会遍历所有元素，不用担心左右孩子有会漏掉的情况
        # heap_insert的时间复杂度是O(log(N))，log(1)+log(2)+...+log(N)在N收敛
        # 所以时间复杂度是N
        size = len(arr)
        for i in range(size):
            cls.heap_insert(arr, i)
        size -= 1
        # 交换第一个和最后一个元素，因为是大顶堆，所以交换后，最后一个元素是最大的
        arr[0], arr[size] = arr[size], arr[0]
        # 交换后需要调整堆
        while size > 0:
            cls.heapify(arr, 0, size)
            size -= 1
            arr[0], arr[size] = arr[size], arr[0]

    @classmethod
    def heap_insert(cls, arr, index):
        # 这里不能用位运算，即index - 1 >> 1,因为当index=0的时候，index-1>>1 的结果是-1，而不是0
        # int((index-1)/2)可以保证小数向零取整
        while arr[index] > arr[int((index-1) / 2)]:
            arr[index], arr[int((index-1) / 2)] = arr[int((index-1) / 2)], arr[index]
            index = int((index-1) / 2)

    @classmethod
    def heapify(cls, arr, index, size):
        left = index * 2 + 1
        while left < size:
            if left + 1 < size and arr[left] < arr[left+1]:
                largest = left + 1
            else:
                largest = left

            largest = index if arr[largest] <= arr[index] else largest
            if largest == index:
                break

            arr[index], arr[largest] = arr[largest], arr[index]

            index = largest
            left = 2 * index + 1


if __name__ == '__main__':
    max_times = 1000
    max_size = 100
    max_value = 100

    res = True

    for _ in range(max_times):
        arr1 = Comparator.gen_random_array(max_size, max_value)
        arr2 = Comparator.copy_arr(arr1)
        HeapSort.heap_sort(arr1)
        sorted_arr2 = sorted(arr2)

        if not Comparator.is_equal(arr1, sorted_arr2):
            res = False
            break

    if not res:
        print('Failed ')
    else:
        print('Success')