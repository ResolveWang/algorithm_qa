# -*- coding:utf-8 -*-
"""
问题: 在股市的交易日中，假设最多可进行两次买卖(即买和卖的次数均小于等于2)，
规则是必须一笔成交后进行另一笔(即买-卖-买-卖的顺序进行)。给出一天中的股票
变化序列，请写一个程序计算一天可以获得的最大收益。请采用实践复杂度低的方法实现。

思路: 以第i天为分界线，计算第i天之前进行一次交易的最大收益preProfit[i]，
和第i天之后进行一次交易的最大收益postProfit[i].最后遍历一遍，
max{preProfit[i] + postProfit[i]} (0≤i≤n-1)就是最大收益。
"""


import sys


class Stock:
    def maxProfit(self, prices, n):
        if n <= 1:
            return 0

        pre_profit = [0 for _ in range(n)]
        post_profit = [0 for _ in range(n)]

        min_buy = prices[0]
        index = 1
        while index < n:
            min_buy = min([prices[index], min_buy])
            pre_profit[index] = max([pre_profit[index - 1], prices[index] - min_buy])
            index += 1

        max_sale = prices[index - 1]
        index = n - 2
        while index >= 0:
            max_sale = max([max_sale, prices[index]])
            post_profit[index] = max([post_profit[index + 1], max_sale - prices[index]])
            index -= 1

        max_profit = -sys.maxsize
        index = 0
        while index < n:
            max_profit = max([pre_profit[index] + post_profit[index], max_profit])
            index += 1

        return max_profit


if __name__ == '__main__':
    solution = Stock()
    print(solution.maxProfit([10, 5, 4, 3, 2, 1], 6))
