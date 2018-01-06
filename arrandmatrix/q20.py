"""
问题描述:有N个长度不一的数组,所有的数组都是有序的,请从大到小打印这N个数组整体
最大的前K个数。

例如:
输入含有N行元素的二维数组可以代表N个一维数组。
219,405,538,845,971
148,558
52,99,348,691
再输入整数K=5,则打印:
Top 5:971,845,691,558,538

要求:
1.如果所有数组的元素个数小于K,则从大到小打印所有的数。
2.要求时间复杂度为O(KlogN)。
"""


class HeapNode:
    def __init__(self, value, arr_num, arr_index):
        self.value = value
        self.arr_num = arr_num
        self.arr_index = arr_index


class TopKPrinter:
    @classmethod
    def print_top_k(cls, arr, k):
        n = len(arr)
        heap = [0 for _ in range(n)]
        for i in range(n):
            arr_index = len(arr[i]) - 1
            node = HeapNode(arr[i][arr_index], i, arr_index)
            heap[i] = node
            cls.heap_insert(heap, i)
        print('Top {}:'.format(k), end='')
        for _ in range(k):
            if n == 0:
                return
            print(heap[0].value, end=' ')
            if heap[0].arr_index != 0:
                arr_num = heap[0].arr_num
                new_arr_index = heap[0].arr_index - 1
                value = arr[arr_num][new_arr_index]
                new_node = HeapNode(value, arr_num, new_arr_index)
                heap[0] = new_node
            else:
                n -= 1
                heap[0], heap[n] = heap[n], heap[0]
            cls.heapify(heap, 0, n)

    @classmethod
    def heap_insert(cls, heap, index):
        while heap[index].value > heap[int((index - 1) / 2)].value:
            heap[index], heap[int((index - 1) / 2)] = heap[int((index - 1) / 2)], heap[index]
            index = int((index - 1) / 2)

    @classmethod
    def heapify(cls, heap, index, size):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        largest = index
        while left_index < size:
            if heap[index].value < heap[left_index].value:
                largest = left_index
            if right_index < size and heap[largest].value < heap[right_index].value:
                largest = right_index

            if largest == index:
                return
            else:
                heap[index], heap[largest] = heap[largest], heap[index]

            index = largest
            left_index = index * 2 + 1
            right_index = index * 2 + 2


if __name__ == '__main__':
    my_matrix = [[219, 405, 538, 845, 971], [148, 558], [52, 99, 348, 691]]
    TopKPrinter.print_top_k(my_matrix, 5)
