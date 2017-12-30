"""
给定一个无序数组arr,求出需要排序的最短子数组长度。
例如:
arr=[1, 5, 3, 4, 2, 6, 7],返回４,因为只有[5, 3, 2, 4]需要排序。
"""
class ShortestSubarr:
    @classmethod
    def get_shortest_subarr(cls, arr):
        if not arr or len(arr) == 1:
            return 0

        length = len(arr)
        max_index = -1
        index = length - 1

        min_value = arr[index]
        while index >= 0:
            if arr[index] <= min_value:
                min_value = arr[index]
            else:
                max_index = index
            index -= 1

        if max_index == -1:
            return 0

        min_index = -1
        index = 0
        max_value = arr[index]
        while index < length:
            if arr[index] >= max_value:
                max_value = arr[index]
            else:
                min_index = index
            index += 1

        return min_index - max_index + 1


if __name__ == '__main__':
    print(ShortestSubarr.get_shortest_subarr([1, 5, 3, 4, 2, 6, 7]))