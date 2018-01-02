"""
BFPRT算法
解决问题：求一个数组中第K大/小的数或者前K小的数。
时间复杂度：O(N)
"""


class BFPRT:
    @classmethod
    def get_the_k_number(cls, arr, k):
        if not arr or len(arr) < k:
            return
        return cls.select(arr, 0, len(arr)-1, k)

    @classmethod
    def select(cls, arr, begin, end, k):
        if begin == end:
            return arr[begin]
        priovt = cls.get_median_of_median(arr, begin, end)
        small, big = cls.patition(arr, begin, end, priovt)
        if small <= k <= big:
            return arr[k]
        elif small > k:
            return cls.select(arr, begin, small-1, k)
        else:
            return cls.select(arr, big+1, end, k)

    @classmethod
    def get_median_of_median(cls, arr, begin, end):
        num = end - begin + 1
        if num % 5 == 0:
            offset = 0
        else:
            offset = 1
        media_arr = list()
        for i in range(offset + int(num/5)):
            begin_index = begin + i * 5
            end_index = begin_index + 4
            mid = cls.get_median_value(arr, begin_index, min([end_index, end]))
            media_arr.append(mid)
        return cls.get_median_value(media_arr, 0, len(media_arr)-1)

    @classmethod
    def get_median_value(cls, arr, begin, end):
        cls.insert_sort(arr, begin, end)
        index = int((end+begin) / 2)
        return arr[index]

    @classmethod
    def patition(cls, arr, begin, end, privot):
        small = begin - 1
        cur = begin
        big = end + 1
        while cur != big:
            if arr[cur] < privot:
                small += 1
                arr[small], arr[cur] = arr[cur], arr[small]
                cur += 1
            elif arr[cur] > privot:
                big -= 1
                arr[big], arr[cur] = arr[cur], arr[big]
            else:
                cur += 1
        return small+1, big-1

    @classmethod
    def insert_sort(cls, arr, begin, end):
        for i in range(begin+1, end+1):
            while i > begin and arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1

        return arr


if __name__ == '__main__':
    print(BFPRT.get_the_k_number([6, 9, 1, 3, 1, 2, 2, 5, 6, 1, 3, 5, 9, 7, 2, 5, 6, 1, 9], 10))

