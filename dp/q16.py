"""
问题描述：给定无序数组arr,返回其中最长的连续序列的长度。

举例：
arr=[100, 4, 200, 1, 3, 2]，最长的连续序列为[1, 2, 3, 4]，所以返回4
"""


class LongestSeq:
    @classmethod
    def get_longest_sequce_from_arr(cls, arr):
        if not arr:
            return 0

        my_dict = dict()
        max_len = 0
        for i in arr:
            if i not in my_dict:
                my_dict[i] = 1
                if i - 1 in my_dict:
                    max_len = max([cls.merge_small(my_dict, i), max_len])
                    #max_len = max([cls.merge(my_dict, i-1, i), max_len])
                if i + 1 in my_dict:
                    max_len = max([cls.merge_big(my_dict, i), max_len])
                    #max_len = max([cls.merge(my_dict, i, i+1), max_len])
        return max_len

    @classmethod
    def merge_small(cls, my_dict, i):
        arr_len = my_dict[i-1]
        arr_len += 1
        left_edge = i - my_dict[i-1]
        my_dict[i] = arr_len
        my_dict[left_edge] = arr_len

        return arr_len

    @classmethod
    def merge_big(cls, my_dict, i):
        left_length = my_dict[i]
        arr_len = my_dict[i+1]
        arr_len += left_length
        right_edge = i + my_dict[i+1]
        my_dict[i-left_length+1] = arr_len
        my_dict[right_edge] = arr_len

        return arr_len

    @classmethod
    def merge(cls, my_dict, less, more):
        left = less - my_dict[less] + 1
        right = more + my_dict[more] - 1
        length = right - left + 1
        my_dict[left] = length
        my_dict[right] = length
        return length


if __name__ == '__main__':
    print(LongestSeq.get_longest_sequce_from_arr([100, 4, 200, 1, 3, 2]))