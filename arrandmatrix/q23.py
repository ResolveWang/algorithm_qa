"""
问题描述:给定一个有序数组arr,调整arr使得这个数组的左半部分没有重复
元素且升序,而不用保证右部分是否有序。

例如:
arr=[1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9],调整之后
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9...]

补充题目:
给定一个数组arr,其中只可能含有0,1,2这三个值,请实现arr的排序.
另一种问法:有一个数组，其中只有红球、蓝球和黄球，请实现红球全部放在数组
的左边，蓝球放在中间，黄球放在右边。
另一种问法:有一个数组，再给定一个值k，请实现比k小的数都放在数组的左边，
等于k的数都放在数组的中间，比k大的数都放在数组的右边。

要求:
1.所有题目实现的时间复杂度为O(N)
2.所有题目实现的额外空间复杂度为O(1)
"""


class PartionProblem:
    @classmethod
    def get_sorted_arr(cls, arr):
        if not arr or arr[0] == arr[-1]:
            return arr

        max_value = arr[-1]

        for i in range(len(arr)):
            if i == 0:
                continue

            tmp = i
            while arr[tmp] <= arr[i-1]:
                tmp += 1
            arr[tmp], arr[i] = arr[i], arr[tmp]
            if arr[i] == max_value:
                break

        return arr

    @classmethod
    def quick_sortt_partion(cls, arr):
        if not arr or len(arr) == 1:
            return arr

        left = -1
        right = len(arr)
        index = 0

        while index != right:
            if arr[index] == 1:
                index += 1
            elif arr[index] == 0:
                left += 1
                arr[index], arr[left] = arr[left], arr[index]
                index += 1
            else:
                right -= 1
                arr[index], arr[right] = arr[right], arr[index]

        return arr


if __name__ == '__main__':
    my_arr = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
    print(PartionProblem.get_sorted_arr(my_arr))

    my_arr2 = [1, 0, 2, 2, 1, 0, 2, 0, 1, 1, 2, 0, 0]
    print(PartionProblem.quick_sortt_partion(my_arr2))
