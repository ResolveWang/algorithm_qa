"""
问题描述：给定一个字符类型的数组chas，请在单词间做逆序调整。只要做到单词顺序逆序即可，
对空格的位置没有特殊要求。

举例：
如果把chas看做字符串为"dog loves pig"，调整成"pig loves dog".
如果把chas看做字符串为"I'm a student"，调整成"student a I'm".

补充题目：
给定一个字符类型的数组chas和一个整数size，请把大小为size的左半区整体移动到右半区，右半
区整体移动到左边。

举例：
如果把chas看做字符串"ABCDE",size=3,调整为"DEABC"

要求：
如果chas长度为N，两道题都要求时间复杂度为O(N)，额外空间复杂度为O(1).
"""


class StrRotation:
    @classmethod
    def get_rotated_chas(cls, chas):
        if not chas:
            return chas

        cls.rotate_all(chas, 0, len(chas)-1)
        index = 0
        latest_space_index = 0
        while index < len(chas):
            if chas[index] == ' ':
                cls.rotate_all(chas, latest_space_index, index-1)
                latest_space_index = index + 1
            index += 1
        cls.rotate_all(chas, latest_space_index, index - 1)
        return chas

    @classmethod
    def rotate_by_size(cls, chas, size):
        if not chas or not size or len(chas) < size:
            return chas
        cls.rotate_all(chas, 0, len(chas)-1)
        length = len(chas)
        left_end_index = length - size - 1
        cls.rotate_all(chas, 0, left_end_index)
        cls.rotate_all(chas, left_end_index+1, len(chas)-1)
        return chas

    @classmethod
    def rotate_all(cls, chas, start, end):
        left_index = start
        right_index = end
        while left_index < right_index:
            chas[left_index], chas[right_index] = chas[right_index], chas[left_index]
            left_index += 1
            right_index -= 1


if __name__ == '__main__':
    print(StrRotation.get_rotated_chas(['d', 'o', 'g', ' ', 'l', 'o', 'v', 'e', 's', ' ', 'p', 'i', 'g']))
    print(StrRotation.rotate_by_size(['1', '2', '3', '4', '5', 'A', 'B', 'C'], 3))