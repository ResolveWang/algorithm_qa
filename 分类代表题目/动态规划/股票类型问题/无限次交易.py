"""
问题: 假设把股票价格按时间先后顺序存储在数组中，可以买卖任意次，请问
该股票可能获得的最大利润是多少？

思路: 贪心算法，当价格了就卖，价格跌了就买
"""


class Stock:
    def maxProfit(self, prices, n):
        if n <= 1:
            return 0

        index = 0
        profit = 0
        while index < n - 1:
            if prices[index] < prices[index + 1]:
                profit += (prices[index + 1] - prices[index])
            index += 1

        return profit


if __name__ == '__main__':
    solution = Stock()
    print(solution.maxProfit([10, 22, 5, 75, 65, 80], 6))
