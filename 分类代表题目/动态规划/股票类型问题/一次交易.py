"""
问题: 假设把股票价格按时间先后顺序存储在数组中，请问买卖
一次该股票可能获得的最大利润是多少？

例子: [9, 11, 8, 5, 7, 12, 16, 14] => 在价格5的时
候买入，在价格16的时候卖出，利润最大，为11
"""


class Stock:
    def maxProfit(self, prices, n):
        if n <= 1:
            return 0

        max_profit = 0
        min_buy = prices[0]

        index = 1
        while index < n:
            min_buy = min([prices[index], min_buy])
            max_profit = max([max_profit, prices[index]-min_buy])
            index += 1

        return max_profit


if __name__ == '__main__':
    solution = Stock()
    print(solution.maxProfit([9, 11, 8, 5, 7, 12, 16, 14], 8))

