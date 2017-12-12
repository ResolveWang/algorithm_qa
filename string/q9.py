"""
问题描述：给定一个字符串数组strs[],在strs中有些位置为None，但在不为None的位置上，
其字符串是按照字典顺序由小到大依次出现的。再给定一个字符串str，请返回str在strs中出
现的最左的位置。

举例：
strs=[None, 'a', None, 'a', None, 'b', None, 'c']，str='a'，返回1.
strs=[None, 'a', None, 'a', None, 'b', None, 'c'], str=None,返回-1
strs=[None, 'a', None, 'a', None, 'b', None, 'c'], str='d',返回-1
"""


class CharFinder:
    @classmethod
    def get_the_leftest_post(cls, strs, char):
        if not char or not strs:
            return -1
        return cls.detail(strs, char, 0, len(strs) - 1)

    @classmethod
    def detail(cls, strs, char, start, end):
        if start > end:
            return -1

        pos = start + ((end - start) >> 1)

        if strs[pos] is None:
            res_left = cls.detail(strs, char, start, pos - 1)
            res_right = cls.detail(strs, char, pos + 1, end)
            if res_left and res_left != -1:
                return res_left
            return res_right

        elif strs[pos] == char:
            last_pos = pos
            while pos >= 0 and (strs[pos] == char or strs[pos] is None):
                if strs[pos] == char:
                    last_pos = pos
                pos -= 1

            return last_pos

        elif strs[pos] > char:
            return cls.detail(strs, char, start, end - 1)
        else:
            return cls.detail(strs, char, start + 1, end)


if __name__ == '__main__':
    arr = [None, "a", None, "a", None, "b", None,
           None, None, "b", None, "c", None, "c", None, None, "d", None,
           None, None, None, None, "d", None, "e", None, None, "e", None,
           None, None, "f", None, "f", None]
    str1 = 'a'
    print(CharFinder.get_the_leftest_post(arr, str1))
    str2 = 'b'
    print(CharFinder.get_the_leftest_post(arr, str2))
    str3 = 'c'
    print(CharFinder.get_the_leftest_post(arr, str3))
    str4 = 'd'
    print(CharFinder.get_the_leftest_post(arr, str4))
    str5 = 'e'
    print(CharFinder.get_the_leftest_post(arr, str5))
    str6 = 'f'
    print(CharFinder.get_the_leftest_post(arr, str6))
    str7 = 'h'
    print(CharFinder.get_the_leftest_post(arr, str7))