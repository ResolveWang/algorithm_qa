"""
问题: 把n个骰子扔在地上，所有的骰子朝上一面的点数之和为s。输入n，打印出
s的所有可能的值出现的概率
"""


class Probability:
    def __init__(self):
        self.max_value = 6

    def get_probability(self, n):
        if n < 1:
            return

        probalities = [0 for _ in range(self.max_value*n-n+1)]

        self.process(n, probalities)
        total = pow(self.max_value, n)
        for index, value in enumerate(probalities):
            print('{}:{}'.format(index+n, round(value/total, 4)))

    def process(self, n, probalities):
        for i in range(1, self.max_value+1):
            self.process_detail(n, i, n-1, probalities)

    def process_detail(self, aim, cur_sum, cur_n, probalities):
        if cur_n == 0:
            probalities[cur_sum-aim] += 1
        else:
            for i in range(1, self.max_value+1):
                self.process_detail(aim, cur_sum+i, cur_n-1, probalities)


if __name__ == '__main__':
    solution = Probability()
    solution.get_probability(2)