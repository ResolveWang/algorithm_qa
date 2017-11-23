"""
问题描述：给定一个字符串str1，只能往str1的后面添加字符变成str2。
要求1：str2必须包含两个str1,两个str1可以有重合，但是不能以同一个位置开头。
要求2：str2尽量短。
最终返回str2.

举例：
str1 = 123, 则str2 = 123123，这时候包含两个str1,且不以相同位置开头，且str2最短。
"""


class ShortestStr:
    @classmethod
    def get_shortest_str(cls, str1):
        if not str1:
            return str1

        if len(str1) == 1:
            return str1 + str1

        if len(str1) == 2:
            if str1[0] == str1[1]:
                return str1 + str1[0]
            else:
                return str1 + str1

        index = cls.find_loggest_prefix(str1)
        return str1 + str1[index:]

    @classmethod
    def find_loggest_prefix(cls, str1):
        length = len(str1)
        next_arr = [0 for _ in range(length+1)]
        next_arr[0] = -1
        next_arr[1] = 0

        pos = 2
        cn = 0

        while pos < len(next_arr):
            if str1[pos-1] == str1[cn]:
                cn += 1
                next_arr[pos] = cn
                pos += 1
            elif cn > 0:
                cn = next_arr[cn]
            else:
                next_arr[pos] = 0
                pos += 1
        return next_arr[-1]


if __name__ == '__main__':
    test1 = "a"
    print(ShortestStr.get_shortest_str(test1))

    test2 = "aa"
    print(ShortestStr.get_shortest_str(test2))

    test3 = "ab"
    print(ShortestStr.get_shortest_str(test3))

    test4 = "abcdabcd"
    print(ShortestStr.get_shortest_str(test4))

    test5 = "abracadabra"
    print(ShortestStr.get_shortest_str(test5))