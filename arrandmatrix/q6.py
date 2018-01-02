"""
问题描述:给定一个整型数组arr,打印其中出现次数大于一半的数,如果没有这样
的数,打印提示信息.

进阶:
给定一个整型数组arr,再给定一个整数k,打印所有出现次数大于N/K的数,如果没有
这样的数,打印提示信息.

要求:
原问题要求时间复杂度为O(N),额外空间复杂度为O(1)。进阶问题要求时间复杂度为
O(M*N),额外空间复杂度为O(K).
"""


class HalfOfTotal:
    @classmethod
    def get_num_more_than_half(cls, arr):
        if not arr:
            print('No that num')
            return

        count = 0
        for i in arr:
            if count == 0:
                candinate = i
            else:
                if i == candinate:
                    count += 1
                else:
                    count -= 1

        count = 0
        for i in arr:
            if i == candinate:
                count += 1

        if int(len(arr)/2) < count:
            print(candinate)
        else:
            print('No than num')


class KOfTotal:
    @classmethod
    def get_nums_more_than_k(cls, arr, k):
        if k < 2:
            print('the k args is invalid')
            return

        candinate_length = k - 1
        candinates = dict()
        for i in arr:
            cur_len = len(candinates)
            if i in candinates.keys():
                candinates[i] += 1
            else:
                if cur_len < candinate_length:
                    candinates[i] = 1
                else:
                    for key in candinates.keys():
                        candinates[key] -= 1
                        if candinates[key] == 0:
                            del candinates[key]

        res = list()
        for candinate in candinates:
            count = 0
            for i in arr:
                if i == candinate:
                    count += 1
            if count > int(len(arr)/k):
                res.append(candinate)

        if not res:
            print('No those nums')
            return

        for i in res:
            print(i, end=' ')


if __name__ == '__main__':
    my_arr = [1, 2, 3, 1, 1, 2, 1]
    k = 4
    HalfOfTotal.get_num_more_than_half(my_arr)
    KOfTotal.get_nums_more_than_k(my_arr, k)