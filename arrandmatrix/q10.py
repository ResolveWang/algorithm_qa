"""
给定一个数组arr，该数组无序，但每个值均为正数，再给定一个正数k。求arr的
所有子数组中所有元素相加和为k的最长子数组长度。
例如，arr=[1, 2, 1, 1, 1]， k=3
累加和为3的最长子数组长度为[1, 1, 1]，所以结果返回3
"""
from array import array


class MaxLength:
    @classmethod
    def get_max_length_for_unsigned_arr(cls, arr, num):
        length = len(arr)
        if length == 0:
            return 0
        left_index = 0
        right_index = 0
        value_total = 0
        values_length = 0
        count = 0
        while right_index < length:
            value_total += arr[right_index]
            count += 1
            if value_total == num:
                if count > values_length:
                    values_length = count
                value_total -= arr[left_index]
                left_index += 1
                count -= 1
            elif value_total > num:
                value_total -= arr[left_index]
                left_index += 1
                count -= 1
            right_index += 1

        return values_length


if __name__ == '__main__':
    cur_arr = array('i', [9, 3, 8, 4, 6, 3, 1, 8, 6, 5, 4, 5, 3, 5, 4, 10, 5, 8, 3, 5])
    print(MaxLength.get_max_length_for_unsigned_arr(cur_arr, 15))