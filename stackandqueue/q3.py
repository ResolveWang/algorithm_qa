"""
问题描述：一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈
转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，要求：
只能用递归函数来实现和初始栈，不能使用其他数据结构，

思路：首先使用一个递归函数获取到栈底元素，再构造另外一个递归函数来进行reverse操作
"""


class ReverseTool:
    @classmethod
    def get_stack_bottom(cls, stack):
        i = stack.pop()
        if len(stack) == 0:
            return i
        else:
            last = cls.get_stack_bottom(stack)
            stack.append(i)
            return last

    @classmethod
    def reverse(cls, stack):
        if len(stack) == 0:
            return
        else:
            i = cls.get_stack_bottom(stack)
            cls.reverse(stack)
            stack.append(i)

if __name__ == '__main__':
    my_stack = [1, 2, 3]
    ReverseTool.reverse(my_stack)
    print(my_stack)
