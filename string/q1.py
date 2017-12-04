"""
问题描述：给定两个字符串str1和str2，如果str1和str2中出现的字符种类一样且每种字符出现
的次数也一样，那么str1和str2互为变形词。请实现函数判断两个字符串是否互为变形词。

举例：
str1='123', str2='231',返回true
str1='123', str2='2331'，返回false
"""


class Words:
    @classmethod
    def is_similar_words(cls, str1, str2):
        if len(str1) != len(str2):
            return False

        my_dict = dict()
        for i in str1:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for j in str2:
            if j not in my_dict:
                return False
            else:
                my_dict[j] -= 1
                if my_dict[j] < 0:
                    return False

        return True


if __name__ == '__main__':
    A = "abcabcabc"
    B = "bcacbaacb"
    print(Words.is_similar_words(A, B))