"""
问题描述：给定字符串str1和str2，求str1的子串中含有str2所有字符的最小子串长度。

举例：
str1='abcde',str2='ac'。因为'abc'包含str2的所有字符，并且在满足这一条件的str1
的所有子串中，'abc'是最短的，返回３．
str1='12345',str2='344'。最小包含子串不存在，返回0.
"""
import sys


class ShortestContainedSubstr:
    @classmethod
    def get_shortest_contained_subsrt(cls, str1, str2):
        if not str1 or not str2 or len(str1) < len(str2):
            return 0

        left = 0
        right = 0
        aim = dict()
        for i in str2:
            if i not in aim:
                aim[i] = 1
            else:
                aim[i] += 1
        short_length = sys.maxsize
        match = len(str2)

        length1 = len(str1)
        length2 = len(str2)
        while right < length1:
            if str1[right] not in aim:
                aim[str1[right]] = -1
            else:
                aim[str1[right]] -= 1
                match -= 1
                if match == 0:
                    short_length = min([short_length, right-left+1])
                    while left <= right:
                        if right - left == length2:
                            return length2
                        if str1[left] not in str2:
                            left += 1
                            aim[str1[left]] += 1
                        else:
                            if aim[str1[left]] == 0:
                                short_length = min([short_length, right - left + 1])
                                break
                            else:
                                left += 1
                                aim[str1[left]] += 1
                    left += 1
            right += 1

        return short_length if short_length != sys.maxsize else 0


if __name__ == '__main__':
    str1 = "adabbca"
    str2 = "acb"
    print(ShortestContainedSubstr.get_shortest_contained_subsrt(str1, str2))