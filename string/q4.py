"""
给定一个字符串str，把字符串str前面任意的部分挪到后面形成的字符串叫做str
的旋转词。比如 str='12345',str的旋转词有'12345'，'23451'，'34512'、
'45123'和'51234'。给定两个字符串a和b，请判断a和b是否互为旋转词。

举例：
a = 'abcd', b = 'cdab'，返回True
a = '1ab2', b = 'ab12', 返回False

要求：
如果a和b长度不一样，那么a和b必然不是旋转词，可以直接返回False。当a和b长度
一样，都为N时，要求解法的时间复杂度为O(N)。
"""


class RotationStr:
    @classmethod
    def is_rotation(cls, str1, str2):
        if len(str1) != len(str2):
            return False

        str1 = str1 * 2
        # 这里如果不用系统调用，那么就用KMP
        if str2 not in str1:
            return False
        return True


if __name__ == '__main__':
    str1 = 'abcdefg123'
    str2 = '123abcdefg'
    print(RotationStr.is_rotation(str1, str2))