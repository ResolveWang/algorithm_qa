"""
问题描述：给定一个字符串数组strs，再给定两个字符串str1和str2,返回在strs中
str1与str2的最小距离，如果str1或者str2为null，或不在strs中，返回-1.

举例：
strs=['1', '3', '3'， '3'， '2'， '3'， '1'],str1='1'，str2='2'，返回2
strs=['CD'],str1='CD',str2='AB'，返回-1

进阶题目：
如果查询发生的次数有很多，如何把每次查询的时间复杂度降为O(1)
"""


import sys


class ShortestDistance:
    @classmethod
    def find_short_distance(cls, strs, str1, str2):
        if not strs or not str1 or not str2 or str1 not in strs or str2 not in strs:
            return -1

        if str1 == str2:
            return 0

        last_index1 = -1
        last_index2 = -1
        min_value = sys.maxsize

        index = 0
        while index < len(strs):
            if strs[index] == str1:
                if last_index2 == -1:
                    pass
                else:
                    min_value = min([index - last_index2, min_value])
                last_index1 = index

            if strs[index] == str2:
                if last_index1 == -1:
                    pass
                else:
                    min_value = min([index - last_index1, min_value])
                last_index2 = index
            index += 1

        return min_value if min_value != sys.maxsize else -1

    @classmethod
    def construct_hash_map(cls, strs):
        length = len(strs)
        outer_index = 0
        hash_map = dict()
        while outer_index < length:
            inner_index = 0
            inner_map = dict()
            while inner_index < length:
                inner_map[strs[inner_index]] = cls.find_short_distance(strs, strs[outer_index], strs[inner_index])
                inner_index += 1
            hash_map[strs[outer_index]] = inner_map
            outer_index += 1
        return hash_map

    @classmethod
    def get_shortest_distance_by_map(cls, strs, str1, str2):
        if not strs or not str1 or not str2 or str1 not in strs or str2 not in strs:
            return -1

        if str1 == str2:
            return 0

        hash_map = cls.construct_hash_map(strs)
        inner_dict = hash_map.get(str1)
        return inner_dict.get(str2)


if __name__ == '__main__':
    strs1 = ["4", "2", "2", "3", "2", "2", "3", "1", "1", "3"]
    print(ShortestDistance.find_short_distance(strs1, '4', '3'))
    print(ShortestDistance.find_short_distance(strs1, '2', '3'))
    print(ShortestDistance.find_short_distance(strs1, '2', '1'))

    print(ShortestDistance.get_shortest_distance_by_map(strs1, '4', '3'))
    print(ShortestDistance.get_shortest_distance_by_map(strs1, '2', '3'))
    print(ShortestDistance.get_shortest_distance_by_map(strs1, '2', '1'))