"""
问题描述：新型字符的定义如下：
１．新型字符是长度为１或者２的字符串
２．表现形式可以仅是小写字母，例如“e”；也可以是大写字母+小写字母，例如
“Ab”;还可以是大写字母+大写字母，例如,“DC”。
现在给定一个字符串str,str一定是若干新型字符正确组合的结果，比如"eaCCBi",
由新型字符"e","a","CC"和"Bi"组成。再给定一个整数k，代表str中的位置。请
返回被k位置指中的新类型字符。

举例：
str="aaABCDEcBCg"。
1. k=7时,返回"Ec"
2. k=4时,返回"CD"
3. k=10时,返回"g"
"""


class NewTypeStr:
    @classmethod
    def get_new_type_str(cls, strs, k):
        if not strs:
            return ''
        if k >= len(strs) or k < 0:
            return ''

        count = 0
        i = k - 1
        while i >= 0:
            if strs[i].isupper():
                count += 1
                i -= 1
            else:
                break
        if count % 2 == 1:
            return strs[k-1:k+1]

        if strs[k].isupper():
            return strs[k:k+2]
        else:
            return strs[k]


if __name__ == '__main__':
    test_str = 'aaABCDEcBCg'
    print(NewTypeStr.get_new_type_str(test_str, 10))
    print(NewTypeStr.get_new_type_str(test_str, 4))
    print(NewTypeStr.get_new_type_str(test_str, 7))