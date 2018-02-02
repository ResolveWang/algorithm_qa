"""
问题描述:一群孩子做游戏,现在请你根据游戏得分来分糖果,要求如下:
1.每个孩子不管得分多少,起码分到１个糖果
2.任意两个相邻的孩子之间,得分较多的孩子必须拿多一些的糖果.
给定一个数组arr代表得分数组,请返回最少需要多少糖果.
例如:arr=[1,2,2],糖果分配为[1,2,1],即可满足要求且数量最少,所以返回4

进阶题目:
原题目中的两个规则不变,再加一条规则:
3.任意两个相邻的孩子之间如果得分一样,糖果数必须相同
给定一个数组arr代表得分数组,返回最少需要多少糖果.
例如,arr=[1,2,2],糖果分配为[1,2,2],即可满足要求且数量最少,所以返回5

要求:
arr长度为N,原题与进阶问题时间复杂度要求为O(N),额外空间复杂度为O(1)
"""


class CandyProblem:
    @classmethod
    def unfair_assign(cls, arr):
        if not arr:
            return 0

        index = cls.get_next_min(arr, 0)
        res = cls.get_right_candies(0, index)
        index += 1
        l_base = 1
        while index != len(arr):
            if arr[index] > arr[index-1]:
                l_base += 1
                res += l_base
                index += 1
            elif arr[index - 1] > arr[index]:
                next_index = cls.get_next_min(arr, index-1)
                r_candies = cls.get_right_candies(index-1, next_index)
                next_index += 1
                r_base = next_index - index + 1
                if r_base > l_base:
                    res += (r_candies - l_base)
                else:
                    res += (r_candies - r_base)

                l_base = 1
                index = next_index
            else:
                index += 1
                res += 1
                l_base = 1

        return res

    @classmethod
    def get_next_min(cls, arr, index):
        while index != len(arr) - 1:
            if arr[index] <= arr[index+1]:
                return index
            index += 1
        return index

    @classmethod
    def get_right_candies(cls, start, end):
        n = end - start + 1
        return int((n*(n+1))/2)

    @classmethod
    def fair_assign(cls, arr):
        if not arr:
            return 0
        index = cls.get_next_min_strict(arr, 0)
        res, rbase = cls.get_candies_and_bases(arr, 0, index)
        index += 1
        same = 1
        lbase = 1
        while index != len(arr):
            if arr[index] > arr[index-1]:
                lbase += 1
                res += lbase
                index += 1
                same = 1
            elif arr[index] < arr[index-1]:
                next_index = cls.get_next_min_strict(arr, index-1)
                candies, rbase = cls.get_candies_and_bases(arr, index-1, next_index)
                if rbase <= lbase:
                    res += (candies - rbase)
                else:
                    res += candies - lbase * same - rbase + rbase * same
                next_index += 1
                lbase = 1
                index = next_index
                same = 1
            else:
                index += 1
                res += lbase
                same += 1

        return res

    @classmethod
    def get_next_min_strict(cls, arr, index):
        while index != len(arr) - 1:
            if arr[index] < arr[index+1]:
                return index
            index += 1
        return index

    @classmethod
    def get_candies_and_bases(cls, arr, start, end):
        base = 1
        candies = 1
        index = end - 1
        while index >= start:
            if arr[index] == arr[index+1]:
                candies += base
            else:
                base += 1
                candies += base
            index -= 1

        return candies, base


if __name__ == '__main__':
    print(CandyProblem.unfair_assign([1, 2, 5, 4, 3, 2, 1]))
    print(CandyProblem.fair_assign([3, 0, 5, 5, 4, 4, 0]))