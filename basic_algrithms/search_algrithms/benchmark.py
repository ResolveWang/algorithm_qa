"""
以系统提供的绝对正确的方法来对比我们自己实现的算法
"""

import random


class Comparator:
    @classmethod
    def compare_with_bench(cls, arr, value):
        """只考虑了基础数据类型"""
        return True if value in arr else False

    @classmethod
    def gen_random_array(cls, max_size, max_value):
        arr = list()
        for _ in range(max_size):
            arr.append(random.randint(1, max_value))

        return sorted(arr)

    @classmethod
    def gen_random_value(cls, max_value):
        return random.randint(1, max_value)