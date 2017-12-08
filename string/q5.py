"""
给定一个字符串str，如果str符合日常书写的整数形式，并且属于32位整数的范围，
返回str所代表的整数值，否则返回0.

举例：
str = '123'，返回123
str = '023'，返回0
str = 'A13'，返回0
str = '0'，返回0
str = '2147483647'，返回2147483647
str = '2147483648'，返回0
str = '-123'，返回-123
"""


class IntegerGenerater:
    @classmethod
    def get_integer(cls, str1):
        if not str1 or str1[0] not in ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 0

        if len(str1) == 1:
            if str1 == '-':
                return 0
            return str1

        for i in str1[1:]:
            if not i.isdigit():
                return 0

        if int(str1) >= 2**31 or int(str1) < -2**31:
            return 0

        return int(str1)


if __name__ == '__main__':
    print(IntegerGenerater.get_integer('2147483647'))
    print(IntegerGenerater.get_integer('-2147483648'))
    print(IntegerGenerater.get_integer('2147483648'))
    print(IntegerGenerater.get_integer('-2147483649'))
    print(IntegerGenerater.get_integer('-123'))