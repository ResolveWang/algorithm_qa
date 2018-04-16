"""
问题:LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看
成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),
“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。
为了方便起见,你可以认为大小王是0
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return False

        numbers.sort()

        index = 0
        total_zero = 0
        pre_num = -1
        while index < 5:
            if numbers[index] == 0:
                total_zero += 1
                index += 1
            else:
                if pre_num != -1:
                    diff = numbers[index] - pre_num
                    if diff == 1:
                        pre_num = numbers[index]
                        index += 1
                    elif diff == 0:
                        return False
                    else:
                        if total_zero < diff-1:
                            return False
                        else:
                            pre_num = numbers[index]
                            total_zero -= (diff -1)
                            index += 1
                else:
                    pre_num = numbers[index]
                    index += 1

        return True


if __name__ == '__main__':
    arr = [0, 3, 2, 6, 4]
    r = Solution().IsContinuous(arr)
    print(r)