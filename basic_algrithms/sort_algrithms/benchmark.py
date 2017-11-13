"""
以系统提供的绝对正确的方法来对比我们自己实现的算法
"""

import copy
import random


class Comparator:
    @classmethod
    def compare_with_bench(cls, arr):
        # 注意这里返回的是一个新数组
        return sorted(arr)

    @classmethod
    def copy_arr(cls, arr):
        return copy.copy(arr)

    @classmethod
    def is_equal(cls, arr1, arr2):
        if (not arr1 and arr2) or (not arr2 and arr1):
            return False

        if not arr1 and not arr2:
            return True

        if len(arr1) != len(arr2):
            return False

        for index, value in enumerate(arr1):
            if arr2[index] != value:
                return False

        return True

    @classmethod
    def gen_random_array(cls, max_size, max_value):
        arr = list()
        for _ in range(max_size):
            arr.append(random.randint(1, max_value))

        return arr

