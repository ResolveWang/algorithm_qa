"""
问题描述：给定一个字符类型数组chas[],判断chas中是否所有字符都只出现过一次，请根据下面
两种不同的要求实现两个函数。

举例：
chas=['a', 'b', 'c']，返回True;chas=['1', '2', '1']，返回False

要求：
1.实现时间复杂度为O(N)的方法。
2.在保证额外空间复杂度为O(1)的前提下，请实现时间复杂度尽量低的方法。
"""


from basic_algrithms.sort_algrithms import heap_sort


class CharHanlder:
    @classmethod
    def handle_meth_1(cls, chas):
        if not chas:
            return True

        res = list()
        for i in chas:
            if i not in res:
                res.append(i)
            else:
                return False

        return True

    @classmethod
    def handle_meth_2(cls, chas):
        if not chas:
            return True

        heap_sort.HeapSort.heap_sort(chas)
        pre = ''
        for i in chas:
            if pre == i:
                return False
            pre = i

        return True


if __name__ == '__main__':
    test_str = ['1', '2', '3', 'a', 'b', 'c', 'd', '4', '5', '6']
    print(CharHanlder.handle_meth_1(test_str))
    print(CharHanlder.handle_meth_2(test_str))
    test_str2 = ['1', '2', '3', 'a', 'b', 'c', 'd', '4', 'a', '6']
    print(CharHanlder.handle_meth_1(test_str2))
    print(CharHanlder.handle_meth_2(test_str2))