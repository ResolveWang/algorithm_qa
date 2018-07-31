"""
问题描述: 牛牛新买了一本算法书，算法书一共有n页，页码从1到n。牛牛于是想了一个算法题目：
在这本算法书页码中0~9每个数字分别出现了多少次？


输入描述:
输入包括一个整数n(1 ≤ n ≤ 1,000,000,000)

输出描述:
输出包括一行10个整数，即0~9这些数字在页码中出现的次数，以空格分隔。行末无空格。
示例1
输入
999
输出
189 300 300 300 300 300 300 300 300 300
"""

# encoding=utf-8


def find(num):
    # 计算每个数字, 在每一位上出现的次数.
    res = [0] * 10  # 结果
    digit = 1  # 个位
    while True:
        low = num % digit
        cur = int((num % (10 * digit)) / digit)
        # 将数字分割, 例如 digit为100时, 表示百位. 12345 将有 high = 12, cur = 3, low = 45
        high = int(num / (10 * digit))
        if cur == 0 and high == 0:
            break

        # 从0到9, 计算i在digit位出现的次数.
        for i in range(10):
            if i < cur:
                if i == 0:
                    res[i] += high * digit
                else:
                    res[i] += (high + 1) * digit
            elif i == cur:
                if i == 0:
                    res[i] += (high - 1) * digit + low + 1
                else:
                    # 比如 12345, i=3, cur=3，那么除了高位1200个，还有低位345+1个
                    res[i] += high * digit + low + 1
            else:
                res[i] += high * digit
        digit *= 10  # 下一位
    return res


num = int(input())
res = find(num)
print(' '.join(map(str, res)))