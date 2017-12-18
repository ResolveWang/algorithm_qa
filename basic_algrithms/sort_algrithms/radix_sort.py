"""
基数排序
"""


class RadisSort:
    @classmethod
    def radis_sort(cls, arr):
        if not arr or len(arr) < 2:
            return arr
        return cls.sort_detail(arr)

    @classmethod
    def sort_detail(cls, arr):
        container = arr
        max_digit = 0
        for i in arr:
            max_digit = max([max_digit, cls.get_digit(i)])
        for i in range(max_digit):
            bucket = [[] for _ in range(10)]
            for j in container:
                digit = cls.get_digit_num(j, i)
                bucket[digit].append(j)
            container = list()
            for j in bucket:
                container.extend(j)
        return container

    @classmethod
    def get_digit(cls, num):
        i = 0
        while num != 0:
            num = int(num/10)
            i += 1
        return i

    @classmethod
    def get_digit_num(cls, num, digit):
        return int((num/10**digit) % 10)


if __name__ == '__main__':
    print(RadisSort.radis_sort([123, 1, 533, 22, 97, 6]))