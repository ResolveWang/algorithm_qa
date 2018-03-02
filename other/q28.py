"""
问题描述:给定两个有序数组arr1和arr2,再给定一个整数k,返回来自arr1和arr2的
两个数相加和最大的前k个,两个数必须分别来自两个数组。

举例:
arr1=[1, 2, 3, 4, 5]
arr2=[3, 5, 7, 9, 11]
k = 4
返回数组[16, 15, 14, 14]

要求:
时间复杂度为O(klogk)
"""


class HeapNode:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


class TOPKSUM:
    @classmethod
    def get_top_k_sum(cls, arr1, arr2, k):
        if not arr1 or not arr2 or k < 1:
            return

        k = min([len(arr1)*len(arr2), k])
        pos_set = set()
        heap = [None for _ in range(k+1)]
        head_r = len(arr1) - 1
        head_c = len(arr2) - 1
        heap_size = 0
        cls.heap_insert(heap, 0, head_r, head_c, arr1[head_r]+arr2[head_c])
        heap_size += 1
        res = list()
        while len(res) < k:
            head = cls.pop_from_head(heap, heap_size)
            heap_size -= 1
            res.append(head.value)
            head_r = head.row
            head_c = head.col

            next1_head_r = head_r - 1
            next1_head_c = head_c
            if head_r and not cls.is_contain(pos_set, next1_head_r, next1_head_c):
                cls.heap_insert(heap, heap_size, next1_head_r, next1_head_c, arr1[next1_head_r]+arr2[next1_head_c])
                heap_size += 1
                cls.add_to_set(pos_set, next1_head_r, next1_head_c)

            next2_head_r = head_r
            next2_head_c = head_c - 1
            if head_c and not cls.is_contain(pos_set, next2_head_r, next2_head_c):
                cls.heap_insert(heap, heap_size, next2_head_r, next2_head_c, arr1[next2_head_r]+arr2[next2_head_c])
                heap_size += 1
                cls.add_to_set(pos_set, next2_head_r, next2_head_c)

        return res

    @classmethod
    def heap_insert(cls, heap: list, index: int, row, col, value)->None:
        node = HeapNode(row, col, value)
        heap[index] = node
        parent_index = int((index-1)/2)
        while index != 0:
            if heap[index].value > heap[parent_index].value:
                heap[index], heap[parent_index] = heap[parent_index], heap[index]
                index = parent_index
                parent_index = int((index-1)/2)
            else:
                break

    @classmethod
    def heapify(cls, arr: list, index: int, size: int)->None:
        left = index * 2 + 1
        while left < size:
            if left + 1 < size and arr[left].value < arr[left+1].value:
                largest = left + 1
            else:
                largest = left

            largest = index if arr[largest].value <= arr[index].value else largest
            if largest == index:
                break

            arr[index], arr[largest] = arr[largest], arr[index]

            index = largest
            left = 2 * index + 1

    @classmethod
    def pop_from_head(cls, heap, heap_size)->HeapNode:
        res = heap[0]
        heap[0], heap[heap_size-1] = heap[heap_size-1], heap[0]
        heap[heap_size-1] = None
        heap_size -= 1
        cls.heapify(heap, 0, heap_size)
        return res

    @classmethod
    def is_contain(cls, datas: set, row, value):
        return '{}_{}'.format(row, value) in datas

    @classmethod
    def add_to_set(cls, datas: set, row: int, col: int)->None:
        datas.add('{}_{}'.format(row, col))


if __name__ == '__main__':
    print(TOPKSUM.get_top_k_sum([1, 2, 3, 4, 5], [3, 5, 7, 9, 11], 4))