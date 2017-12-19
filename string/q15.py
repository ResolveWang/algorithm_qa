"""
问题描述：给定一个字符串str,str表示一个公式，公式里可能有整数，加减乘除符号和
左右括号，返回公式的计算结果。

举例：
str="48*((70-65)-43)+8*1",返回-1816.
str="3+1*4",返回7。
str="3+(1*4)",返回7。

说明：
1.可以认为给定的字符串一定是正确的公式，即不需要对str做公式有效性检查。
2.如果是负数，就需要用括号括起来，比如"4*(-3)"。但是如果负数作为公式的开头或者括号
部分的开头，则可以没有括号，比如"-3*4"和"(-3*4)"都是合法的。
3.不用考虑计算过程中发生溢出的情况。
"""


class Evaler:
    @classmethod
    def str_to_value(cls, strs):
        arrs = cls.convert2arr(strs)
        postfix = cls.convert2postfix(arrs)
        print(postfix)
        value_stack = list()
        for i in postfix:
            if isinstance(i, int):
                value_stack.append(i)
            else:
                if len(value_stack) < 2:
                    if i == '-':
                        value = -value_stack.pop()
                    else:
                        break
                else:
                    pre_2 = value_stack.pop()
                    pre_1 = value_stack.pop()

                    if i == '+':
                        value = pre_1+pre_2
                    elif i == '-':
                        value = pre_1-pre_2
                    elif i == '*':
                        value = pre_1*pre_2
                    else:
                        value = pre_1 / pre_2
                value_stack.append(value)
        return value_stack.pop()

    @classmethod
    def convert2arr(cls, strs):
        tmp = 0
        count = 0
        pre = False
        res = list()
        for i in strs:
            if i.isdigit():
                tmp = tmp * (10 ** count) + int(i)
                if pre:
                    res.pop()
                    res.append(tmp)
                else:
                    res.append(tmp)
                    pre = True
                count += 1
            else:
                tmp = 0
                count = 0
                pre = False
                res.append(i)

        return res

    @classmethod
    def convert2postfix(cls, arr):
        oper = list()
        output = list()
        for i in arr:
            if isinstance(i, int):
                output.append(i)
            elif i in ['+', '-', '*', '/']:
                if not oper:
                    oper.append(i)
                elif i in ['+', '-']:
                    while len(oper) > 0:
                        j = oper[-1]
                        if j != '(':
                            oper.pop()
                            output.append(j)
                        else:
                            break
                    oper.append(i)
                elif i in ['*', '/']:
                    if oper[-1] in ['*', '/']:
                        output.append(oper.pop())
                    oper.append(i)
            elif i == '(':
                oper.append(i)
            else:
                while True:
                    j = oper.pop()
                    if j == '(':
                        break
                    else:
                        output.append(j)

        while len(oper) > 0:
            output.append(oper.pop())

        return output


if __name__ == '__main__':
    strs = '-3*4+5'
    print(Evaler.str_to_value(strs))