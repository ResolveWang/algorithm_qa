"""
问题描述: 你就是一个画家！你现在想绘制一幅画，但是你现在没有足够颜色的颜料.
为了让问题简单，我们用正整数表示不同颜色的颜料。你知道这幅画需要的n种颜色的颜料，
你现在可以去商店购买一些颜料，但是商店不能保证能供应所有颜色的颜料，所以你需要
自己混合一些颜料。混合两种不一样的颜色A和颜色B颜料可以产生(A XOR B)这种颜色的
颜料(新产生的颜料也可以用作继续混合产生新的颜色,XOR表示异或操作)。本着勤俭节约
的精神，你想购买更少的颜料就满足要求，所以兼职程序员的你需要编程来计算出最少需要
购买几种颜色的颜料？

输入描述:
第一行为绘制这幅画需要的颜色种数n (1 ≤ n ≤ 50)
第二行为n个数xi(1 ≤ xi ≤ 1,000,000,000)，表示需要的各种颜料.

输出描述:
输出最少需要在商店购买的颜料颜色种数，注意可能购买的颜色不一定会使用在画中，只是为了产生新的颜色。
示例1
输入
3
1 7 3
输出
3
"""


def getHighPosition(number):
    count = 0
    while number > 0:
        number = number >> 1
        count += 1
    return count


n = int(input())
colors = list(map(int, input().strip().split()))
colors.sort()
lastIndex = len(colors) - 1
bLastIndex = lastIndex - 1
num = 0
while len(colors) > 2:
    if getHighPosition(colors[lastIndex]) == getHighPosition(colors[bLastIndex]):
        temp = colors[lastIndex] ^ colors[bLastIndex]
        if temp not in colors:
            colors.append(temp)
            colors.sort()
            lastIndex += 1
            bLastIndex += 1
    else:
        num += 1
    colors.pop()
    lastIndex -= 1
    bLastIndex -= 1

print(num + len(colors))