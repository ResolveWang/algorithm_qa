"""
定义回文数的概念如下:
如果一个非负数左右完全对应,则该数是回文数,例如:121,22等
如果一个负数的绝对值左右完全对应,也是回文数,例如:-121,-22等
给定一个32位整数num,判断num是不是回文数
"""
import sys


class PalindromeJudger:
    @classmethod
    def is_palindrome(cls, num):
        if num == -sys.maxsize:
            return False

        num = abs(num)

        high_pos = 1
        cur = 9
        while cur/num < 1:
            cur += 9 * pow(10, high_pos)
            high_pos += 1

        while num != 0:
            high_num = int(num / pow(10, high_pos-1))
            low_num = num % 10
            if high_num != low_num:
                return False
            num = int((num - (high_num * pow(10, high_pos-1) - low_num))/10)
            high_pos -= 2

        return True


if __name__ == '__main__':
    print(PalindromeJudger.is_palindrome(12321))
    print(PalindromeJudger.is_palindrome(12320))
    print(PalindromeJudger.is_palindrome(22))



