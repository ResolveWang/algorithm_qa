"""
给定一个字符串str，str全部由数字字符组成，如果str中某一个或某相邻两个字符组成
的子串值在1~26之间，则这个子串可以转换成一个字母，规定1转换为A,2转换为B,3转换
为C...26转换为Z，写一个函数，求str有多少种不同的转换结果，并返回种数。

举例：
str="1111"
能转换出来的结果有"AAAA"、"LAA"、"ALA"、"AAL"和"LL"，返回5.
str="01"
"0"没有对应的字母，而"01"根据规定不可转换，返回0.
str="10"
能转换出的结果是"J",返回1:
"""


class TotalNumForChar:
    @classmethod
    def find_total_num_by_recurise(cls, str1):
        if not str1:
            return 0

        return cls.process(str1, 0)

    @classmethod
    def process(cls, str1, index):
        if index == len(str1):
            return 1
        if str1[index] == '0':
            return 0

        res = cls.process(str1, index+1)
        if index + 1 < len(str1) and int(str1[index])*10 + int(str1[index+1]) < 27:
            res += cls.process(str1, index+2)

        return res


if __name__ == '__main__':
    my_str = "781231783161018231"
    print(TotalNumForChar.find_total_num_by_recurise(my_str))