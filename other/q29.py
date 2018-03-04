"""
问题描述:给定String类型的数组strArr,再给定整数k,请严格按照排名顺序打印
出现次数前k名的字符串

举例:
str=['1', '2', '3', '4'], k=2
No1:1, times: 1
No2:2, times: 1
这种情况下，所有字符串出现一样多，随便打印任何两个字符串都可以

str=['1', '1', '2', '3']
输出:
No1:1, times: 2
No2:2, times: 1
或者:
No1:1, times: 2
No2:3, times: 1

要求:
如果strArr长度为N,时间复杂度请达到O(Nlogk)

进阶题目:
设计并实现TopKRecord结构，可以不断地向其中加入字符串，并且可以根据字符串出现的
情况随时打印加入次数最多前k个字符串，具体为:
1.k在TopKRecord实例生成时指定，并且不再变化(k是构造函数的参数)
2.含有add(String str)方法,即向TopKRecord中加入字符串
3.含有printTopK()方法，即打印加入次数最多的前k个字符串,打印有哪些字符串和对应的
次数即可，不要求严格按排名顺序打印
举例:
record = TopKRecord(2)
record.add('A')
record.print_top_k()
输出:
TOP:
Str: A Times: 1

record.add('B')
record.add('B')
record.print_top_k()
输出:
TOP:
Str:A Times: 1
str:B Times: 2
或者
TOP:
Str:B Times: 2
Str:A Times: 1

record.add('C')
record.add('C')
record.print_top_k()
输出:
TOP:
Str:B Times: 2
Str:C Times: 2
或者
TOP:
Str:C Times: 2
Str:B Times: 2

要求:
1.在任何时刻，add方法的时间复杂度不超过O(logk)
2.在任何时刻，print_top_k方法的时间复杂度不超过O(k)
"""


class HeapNode:
    def __init__(self, string, times):
        self.string = string
        self.times = times


class TOKTimesPrinter:
    @classmethod
    def print_top_k(cls, str_arr: list, k)->None:
        if not str_arr or k < 1:
            return

        word_counts = dict()
        for i in str_arr:
            if i in word_counts:
                word_counts[i] += 1
            else:
                word_counts[i] = 1

        k = min([len(word_counts), k])

        heap = list()
        index = 0
        for key, value in word_counts.items():
            node = HeapNode(key, value)
            if index < k:
                heap.append(node)
                cls.heap_insert(heap, index)
                index += 1
            else:
                if value > heap[0].times:
                    heap[0] = node
                    cls.heapify(heap, 0, k)

        for i in range(len(heap)-1, -1, -1):
            heap[i], heap[0] = heap[0], heap[i]
            cls.heapify(heap, 0, i)

        print('TOP:')
        for node in heap:
            print('Str:{} Times:{}'.format(node.string, node.times))

    @classmethod
    def heapify(cls, heap, index, size):
        left_index = index * 2 + 1
        smallest_index = index
        while left_index < size:
            if heap[left_index].times < heap[smallest_index].times:
                smallest_index = left_index

            if left_index + 1 < size and heap[left_index+1].times < heap[smallest_index].times:
                smallest_index = left_index + 1

            if smallest_index == index:
                return

            heap[smallest_index], heap[index] = heap[index], heap[smallest_index]
            index = smallest_index
            left_index = index * 2 + 1

    @classmethod
    def heap_insert(cls, heap, index):
        while index > 0:
            parent_index = int((index - 1) / 2)
            if heap[parent_index].times > heap[index].times:
                heap[index], heap[parent_index] = heap[parent_index], heap[index]
                index = parent_index
            else:
                break


class TOPKRecord:
    def __init__(self, k):
        self.k = k
        self.heap = list()
        self.str_node_map = dict()
        self.node_index_map = dict()

    def add(self, mystr: str):
        if mystr not in self.str_node_map:
            node = HeapNode(mystr, 1)
            self.str_node_map[mystr] = node
        else:
            node = self.str_node_map[mystr]
            node.times += 1

        pos = self.node_index_map.get(node)
        if pos is not None and pos != -1:
            self.heapify(pos)
        else:
            if len(self.heap) < self.k:
                self.heap.append(node)
                index = len(self.heap) - 1
                self.node_index_map[node] = index
                self.heap_insert(index)
            else:
                if node.times > self.heap[0].times:
                    self.heap[0] = node
                    self.node_index_map[node] = 0
                    self.heapify(0)
                else:
                    self.node_index_map[node] = -1

    def print_top_k(self):
        print('TOP')
        for i in self.heap:
            print('Str:{} Times:{}'.format(i.string, i.times))

    def heapify(self, index):
        size = len(self.heap)
        left_index = index * 2 + 1
        smallest_index = index
        while left_index < size:
            if self.heap[smallest_index].times > self.heap[left_index].times:
                smallest_index = left_index
            if left_index + 1 < size and self.heap[smallest_index].times > self.heap[left_index+1].times:
                smallest_index = left_index + 1

            if smallest_index == index:
                return

            self.swap_two_node(index, smallest_index)
            index = smallest_index
            left_index = index * 2 + 1

    def swap_two_node(self, index1, index2):
        node1 = self.heap[index1]
        node2 = self.heap[index2]
        node1, node2 = node2, node1
        self.node_index_map[node1] = index2
        self.node_index_map[node2] = index1

    def heap_insert(self, index):
        parent_index = int((index-1)/2)
        while index > 0 and self.heap[index].times < self.heap[parent_index].times:
            self.swap_two_node(index, parent_index)
            index = parent_index


if __name__ == '__main__':
    strs = ['1', '1', '2', '3']
    TOKTimesPrinter.print_top_k(strs, 2)

    record = TOPKRecord(2)
    record.add('A')
    record.add('B')
    record.add('B')
    record.add('C')
    record.add('C')
    record.print_top_k()