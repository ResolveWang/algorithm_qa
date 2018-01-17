"""
问题描述:给定一个长度为N且没有重复元素的数组arr和一个整数n,实现函数等概率随机打印
arr中的m个数

要求:
1.相同的数不重复打印
2.时间复杂度为O(M),额外空间复杂度为O(1)
3.可以改变arr数组
"""
import random


class RandomPrinter:
    @classmethod
    def print_random_value(cls, arr, m):
        if not arr or m < 0:
            return

        length = min([len(arr), m])

        for i in range(length):
            random_index = random.randint(0, len(arr)-1-i)
            print(arr[random_index])
            arr[random_index], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[random_index]


if __name__ == '__main__':
    RandomPrinter.print_random_value([1, 2, 3, 4, 5], 5)