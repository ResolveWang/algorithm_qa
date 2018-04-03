"""
给定一个数字，我们按照下面规则将其翻译成字符串:
0翻译成"a",1翻译成"b",...25翻译成"z"，一个数字可能有多种翻译，比如
12258有5种不同的翻译，分别是"bccfi","bwfi","bczi","mcfi"和"mzfi"，
求给定一个数字它的翻译方法有多少种？

思路:
套路就是求以每个位置结尾的情况有多少种翻译方式，可以通过动态规划求解
dp[i] = dp[i-1] + tmp(tmp=dp[i-2]当num_str[index-1:index+1]可以
被翻译成合法的字符，否则tmp为0)
"""


class Num2Str:
    def get_total_res(self, num):
        if num < 0:
            return 0
        if len(str(num)) == 1:
            return 1

        str_num = str(num)
        dp = [0 for _ in range(len(str_num))]
        dp[0] = 1
        if int(str_num[0:2]) > 25:
            dp[1] = 1
        else:
            dp[1] = 2

        index = 2
        while index < len(str_num):
            tmp = 0
            if int(str_num[index-1: index+1]) <= 25:
                tmp = dp[index-2]
            dp[index] = dp[index-1] + tmp
            index += 1

        return dp[-1]


if __name__ == '__main__':
    print(Num2Str().get_total_res(12258))