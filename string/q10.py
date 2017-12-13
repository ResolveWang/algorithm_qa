"""
问题描述：给定一个字符类型的数组chas[],chas右半区全是空字符，左半区不含空字符。
现在想将左半区中所有的空格字符替换成"%20",假设chas右半区足够大，可以满足替换所
需要的空间，请完成替换函数。

举例：
如果把chas的左半区看做字符串，为"a b  c"，假设chas的右半区足够大。替换后，chas
的左半区为"a%20%b%20%20c"

要求：
替换函数时间复杂度为O(N),额外空间复杂度为O(1)

补充题目：
给定一个字符类型的数组chas[],其中只含有数字字符和"*"。现在想把所有的"*"字符挪到
chas的左边，数字字符挪到chas的右边，请完成调整函数。

举例：
如果把chas看做字符串，为"12**345"，调整后chas为"**12345"

要求：
1.调整函数的时间复杂度为O(N)，额外空间复杂度为O(1)。
2.不得改变数字字符从左到右出现的顺序。
"""


class ChasHandler:
    @classmethod
    def solve_problem1(cls, chas):
        if not chas:
            return chas

        num = 0
        length = 0
        for i in chas:
            if i == '':
                break

            if i == ' ':
                num += 1
            length += 1

        last_index = length + num * 2 - 1

        for i in chas[:length][::-1]:
            if i == ' ':
                chas[last_index] = '0'
                last_index -= 1
                chas[last_index] = '2'
                last_index -= 1
                chas[last_index] = '%'
                last_index -= 1
            else:
                chas[last_index] = i
                last_index -= 1

        return chas

    @classmethod
    def solve_problem2(cls, chas):
        if not chas:
            return chas

        cur_index = 0
        latest_index = 0
        length = len(chas)
        while cur_index < length:
            if chas[cur_index] == '*':
                chas[cur_index], chas[latest_index] = chas[latest_index], chas[cur_index]
                latest_index += 1
            cur_index += 1

        return chas


if __name__ == '__main__':
    print(ChasHandler.solve_problem1(['a', ' ', 'b', ' ', ' ', 'c', '', '', '', '', '', '', '', '']))
    print(ChasHandler.solve_problem2(['1', '2', '*', '*', '3', '4', '5']))
