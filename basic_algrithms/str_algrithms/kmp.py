"""
KMP算法
"""


class KMP:
    @classmethod
    def get_index(cls, str1, str2):
        if not str1 or not str2 or len(str1) < len(str2):
            return -1

        next_arr = cls.get_next_arr(str2)
        str1_index = 0
        str2_index = 0

        while str1_index < len(str1) and str2_index < len(str2):
            # 如果匹配上了，两个下标同时移动
            if str1[str1_index] == str2[str2_index]:
                str1_index += 1
                str2_index += 1
            # 如果是str2的第一个字符
            elif next_arr[str2_index] == -1:
                str1_index += 1
            # 如果str1_index和str2_index的位置没配上，那么把str2向右滑动str2_index个
            # 位置再和str1_index匹配
            else:
                str2_index = next_arr[str2_index]

        return str1_index - str2_index if str2_index == len(str2) else -1

    @classmethod
    def get_next_arr(cls, str2):
        length = len(str2)
        if length < 2:
            return [-1]

        next_arr = [0 for _ in range(length)]
        next_arr[0] = -1
        # 下标当前位置
        pos = 2
        # 最长前缀
        cn = 0

        while pos < length:
            # pos位置的字符能匹配上，直接加
            if str2[pos - 1] == str2[cn]:
                cn += 1
                next_arr[pos] = cn
                pos += 1
            # 往回跳，直到跳到0，则一个都未能匹配
            elif cn > 0:
                cn = next_arr[cn]
            else:
                next_arr[pos] = 0
                pos += 1
        print(next_arr)
        return next_arr


if __name__ == '__main__':
    my_str = "abcabcababaccc"
    match = "ababa"
    print(KMP.get_index(my_str, match))