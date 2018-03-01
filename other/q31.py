"""
问题描述:给定两个字符串str和match,长度分别为M和N,实现一个算法,如果字符串str
中含有子串match,则返回match在str中的开始位置,不含有则返回-1

要求:
算法时间复杂度为O(N)
"""


class KMP:
    @classmethod
    def get_index(cls, search_str, match):
        if not search_str or not match or len(search_str) < len(match):
            return -1

        index = 0
        mindex = 0
        next_arr = cls.get_next_arr(match)
        while index < len(search_str) and mindex < len(match):
            if search_str[index] == match[mindex]:
                index += 1
                mindex += 1
            else:
                # match往回跳直到不能再跳，直观上来说就是将match向前推next_arr[mindex]
                # 这样再将mindex和index位置进行比较，而mindex之前部分由于最长前缀和后缀匹配就不必再验证
                if next_arr[mindex] > -1:
                    mindex = next_arr[mindex]
                else:
                    index += 1

        if mindex == len(match):
            return index - mindex
        return -1

    @classmethod
    def get_next_arr(cls, match):
        if len(match) == 1:
            return [-1]

        arr = [0 for _ in range(len(match))]
        arr[0] = -1
        arr[1] = 0
        index = 2
        cursor = 0
        while index < len(match):
            if match[index-1] == match[cursor]:
                arr[index] = cursor + 1
                index += 1
                cursor += 1
            else:
                if cursor == 0:
                    arr[index] = 0
                    index += 1
                else:
                    # 和kmp匹配过程一样，也直接往前跳
                    cursor = arr[cursor]
        return arr


if __name__ == '__main__':
    print(KMP.get_index('acbc', 'bc'))