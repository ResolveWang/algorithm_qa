"""
问题描述:给定一个字符串str,返回str中最长回文子串的长度。
举例:
str='123',其中最长回文子串为1,2,或者3,所以返回1
str='abc1234321ab',其中最长的回文子串为'1234321',所以返回7

进阶:
给定一个字符串str,通过添加字符串让str整体都变成回文串，要求只能在
str的末尾添加字符，请返回在str后面添加的最短字符串

举例:
str='12' => '1'

要求:
如果str长度为N,要求原问题和进阶问题的时间复杂度为O(N)
"""
import sys


class Manacher:
    @classmethod
    def str2manacher(cls, mystr):
        new_str = '#'
        for i in mystr:
            new_str += '%s#' % i
        return new_str

    @classmethod
    def get_max_num(cls, mystr):
        if not mystr:
            return 0

        mystr = cls.str2manacher(mystr)
        center = -1
        right = -1
        str_len = len(mystr)
        arr = [0 for _ in range(str_len)]
        i = 0
        max_value = -sys.maxsize
        while i < str_len:
            # 如果i在r外部，直接向右移动i
            if i > right:
                arr[i] = 1
            else:
                # 2*center-i是i关于center的对称点,right-i是i到r的范围
                # 这一步是找出肯定合法的回文半径
                arr[i] = min([arr[2*center-i], right-i])
            # 对所有情况都直接往两边扩,扩不动就会停止
            while arr[i] + i < str_len and i - arr[i] > -1:
                if mystr[arr[i]+i] == mystr[i-arr[i]]:
                    arr[i] += 1
                else:
                    break
            # arr[i]+i表示i所在的回文右边界，和已知的进行比较
            if arr[i] + i > right:
                right = i + arr[i]
                center = i
            # 得到最大的回文半径
            max_value = max([max_value, arr[i]])

            i += 1
        # 经过处理后的最长回文串必定是以#为中心点的字符串,因此需要-1
        return max_value - 1

    @classmethod
    def get_shortest_str(cls, instr):
        if not instr:
            return

        mystr = cls.str2manacher(instr)
        center = -1
        right = -1
        str_len = len(mystr)
        arr = [0 for _ in range(str_len)]
        i = 0
        left = 0
        while i < str_len:
            if i > right:
                arr[i] = 1
            else:
                arr[i] = min([arr[2*center-i], right-i])

            while arr[i] + i < str_len and i - arr[i] > -1:
                if mystr[arr[i]+i] == mystr[i-arr[i]]:
                    arr[i] += 1
                else:
                    break

            if arr[i] + i > right:
                right = i + arr[i]
                center = i
            # right　＝＝str_len表示已经到了右边界，通过while循环可以看出
            if right == str_len:
                left = arr[i]
                break

            i += 1

        return instr + instr[:len(instr)+1-left][::-1]


if __name__ == '__main__':
    cur_str = 'abc12321'
    print(Manacher.get_max_num(cur_str))

    cur_str = 'abc12321'
    print(Manacher.get_shortest_str(cur_str))