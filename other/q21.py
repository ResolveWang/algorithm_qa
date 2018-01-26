"""
问题描述:给定一个32位整数num,写两个函数分别返回num的英文和中文表达字符串.

举例:
num=319
英文表达为:Three Hundred Nineteen
中文表达为:三百一十九

num=1014
英文表达为:One Thousand Fourteen
中文表达为:一千零一十四

num=-2147483648
英文表达为:Negative,Two Billion,One Hundred Forty Seven Million,Four
Hundred Eighty Three Thousand,Six Hundred Forty Eight
中文表达为:负二十一亿四千七百四十八万三千六百四十八

num=0
英文表达为:Zero
中文表达为:零
"""


class Number2StrEn:
    mapper = ["One ", "Two ", "Three ", "Four ", "Five ", "Six ",
              "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
              "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Sixteen ",
              "Eighteen ", "Nineteen "]

    ten_mapper = ["Twenty ", "Thirty ", "Forty ", "Fifty ",
                  "Sixty ", "Seventy ", "Eighty ", "Ninety "]

    @classmethod
    def num1to19(cls, num):
        if num < 1 or num > 19:
            return ''

        return cls.mapper[num - 1]

    @classmethod
    def num1to99(cls, num):
        if num < 1 or num > 99:
            return ''
        if num < 20:
            return cls.num1to19(num)
        high_pos = int(num / 10)
        return cls.ten_mapper[high_pos - 2] + cls.num1to19(num % 10)

    @classmethod
    def num1to999(cls, num):
        if num < 1 or num > 999:
            return ''
        if num < 100:
            return cls.num1to99(num)

        high_pos = int(num / 100)
        return cls.mapper[high_pos - 1] + 'Hundred ' + cls.num1to99(num % 100)

    @classmethod
    def numtoen(cls, num):
        res = ''
        if num == 0:
            return 'Zero'
        elif num < 0:
            res = 'Negtive, '

        billion = 1000000000
        million = 1000000
        thousand = 1000

        high_pos = int(num / billion)
        if high_pos > 0:
            res += (cls.num1to19(high_pos) + 'Billion,')
            num -= high_pos * billion

        high_pos = int(num/million)
        if high_pos > 0:
            res += (cls.num1to999(high_pos) + 'Million,')
            num -= high_pos * million

        high_pos = int(num/thousand)
        if high_pos > 0:
            res += (cls.num1to999(high_pos) + 'Thousand,')
            num -= high_pos * thousand

        res += cls.num1to999(num)

        return res


if __name__ == '__main__':
    print(Number2StrEn.numtoen(0))
    print(Number2StrEn.numtoen(23))
    print(Number2StrEn.numtoen(233))
    print(Number2StrEn.numtoen(1239406328))

