"""
问题描述:一个char类型的数组chs,其中所有的字符都不同。例如,chs=['A', 'B', 'C'...'Z'],
则字符串与整数的对应关系如下:
A,B...Z,AA,AB...AZ,BA,BB...ZZ,AAA...ZZZ,AAAA...
1,2...26,27,28...52,53,54...702,703...18278,18279...
例如,chs=['A','B','C'],则字符串与整数的对应关系如下:
A,B,C,AA,AB..CC,AAA...CCC,AA AA...
1,2,3,4,5...12,13...39,40...
给定一个数组chs,实现根据对应关系完成字符串与整数相互转换的两个函数.
"""


class ChsIntegerSwitcher:
    @classmethod
    def chs_to_int(cls, arr, string):
        value = 1
        chs_dict = dict()
        base_num = len(arr)
        for i in arr:
            chs_dict[i] = value
            value += 1

        high_pos = len(string) - 1
        res = 0
        cur_pos = 0
        while cur_pos <= high_pos:
            cur_value = chs_dict.get(string[cur_pos])
            res = res + (cur_value * pow(base_num, cur_pos))
            cur_pos += 1
        return res

    @classmethod
    def int_to_chs(cls, arr, num):
        value = 1
        chs_dict = dict()
        base_num = len(arr)
        for i in arr:
            chs_dict[value] = i
            value += 1

        # 最高次幂
        high_pos = 0
        cur_sum = 0
        while cur_sum <= num:
            cur_sum += pow(base_num, high_pos)
            high_pos += 1

        high_pos -= 1
        chs = list()
        while high_pos >= 1 and num > 0:
            tmp = pow(base_num, high_pos-1)
            tmp_count = 0
            left = num

            while left >= 0 and tmp_count <= base_num:
                left = left - tmp
                tmp_count += 1

            tmp_count -= 1
            chs.append(chs_dict.get(tmp_count))
            num -= tmp * tmp_count
            high_pos -= 1
        print(chs)
        return chs


if __name__ == '__main__':
    ChsIntegerSwitcher.chs_to_int(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                                   'X', 'Y', 'Z'], 'ZZZ')

    ChsIntegerSwitcher.chs_to_int(['A', 'B', 'C'], 'ABBA')
    ChsIntegerSwitcher.int_to_chs(['A', 'B', 'C'], 4)
    ChsIntegerSwitcher.int_to_chs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 18277)
